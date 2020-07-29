import logging
import sys
from datetime import timedelta, datetime
from hashlib import sha1

import yaml

from constants import *
import lcg_generator.random as lcg
from query_writer.writer import sql_insert

CURRENCY_PAIR_NAME = 0
CURRENCY_PAIR_VALUE = 1
ORDER_ID_INCREMENT_RANGE = 3, 10
PX_DEFAULT_ROUND = 6
PX_DELTA_RANGE = 0.000001, 0.00001
VOL_DEFAULT_ROUND = 4
NUMBER_OF_TAGS_PER_ORDER = 1, 2
RANDOM_VOL_RANGE = 1, 1000
RANDOM_EXTRA_DATA_HASH_RANGE = 1, 2000

# 30-60 seconds as microseconds
TIME_DELTA = 30000000, 60000000
TIME_DELTA_BETWEEN_STATUS = 100, 999999

"""Init"""
result_list = []

"""Setup"""
logging.basicConfig(level=LOG_DEFAULT_LOGGING_LEVEL, filename=LOG_FILENAME, format=LOG_DEFAULT_FORMAT)
logger = logging.getLogger(APP_NAME)
logger.info('logger set up at %s, writing %s' % (logger.name, LOG_FILENAME))

data_file = open(ORDER_GENERATOR_DATA_ABS_PATH)
generator_data_dict = yaml.load(data_file, Loader=yaml.FullLoader)
sql_dump = open(DUMP_FILENAME, 'w')

TOTAL_ORDERS = generator_data_dict[TOTAL_ORDERS_KEY]
INITIAL_ORDER_ID = generator_data_dict[INITIAL_ORDER_ID_KEY]
PROVIDER_ID_LIST = generator_data_dict[PROVIDER_ID_KEY]
DIRECTION_LIST = generator_data_dict[DIRECTION_KEY]
CURRENCY_PAIR_LIST = list(generator_data_dict[CURRENCY_PAIR_KEY].items())
TAGS_LIST = generator_data_dict[TAGS_KEY]
ZONES = generator_data_dict[ZONES_KEY]


# Incremental fields
def get_initial_order_id_as_decimal(initial_order_id_string: str):
    return int(initial_order_id_string, 16)


def order_id_incrementer(initial_order_id: int):
    order_id = initial_order_id
    yield order_id
    while True:
        order_id += lcg.randint(*ORDER_ID_INCREMENT_RANGE)
        yield order_id


def random_provider_id(provider_id_list: list):
    return lcg.choice(provider_id_list)


def random_direction(random_direction_list: list):
    return lcg.choice(random_direction_list)


def random_currency_pair(currency_pairs_list: list):
    currency_pair = lcg.choice(currency_pairs_list)
    currency = currency_pair[CURRENCY_PAIR_NAME]
    px_init = currency_pair[CURRENCY_PAIR_VALUE]
    px = round(lcg.randomly_modify_value(px_init, *PX_DELTA_RANGE), PX_DEFAULT_ROUND)
    return [currency, px]


def random_vol(vol_min: int, vol_max: int):
    return lcg.randint(vol_min, vol_max)


def random_tags(tags_list: list):
    return lcg.sample(tags_list, lcg.randint(*NUMBER_OF_TAGS_PER_ORDER))


def random_description():
    pass
    return None


def random_extra_data(value):
    return sha1(bytes(value)).hexdigest()


# Dynamic (zone specific) fields
def get_zone_total_orders(zone: dict, total_orders: int):
    return int(total_orders * zone[ZONE_PERCENT_OF_TOTAL_ORDERS_KEY])


def get_zone_initial_date(zone: dict):
    return datetime.strptime(zone[ZONE_INITIAL_DATE_KEY], DEFAULT_DATE_FORMAT)


def get_zone_end_date(zone: dict):
    return datetime.strptime(zone[ZONE_END_DATE_KEY], DEFAULT_DATE_FORMAT)


def get_zone_time_step(zone: dict, total_orders: int):
    return (get_zone_end_date(zone) - get_zone_initial_date(zone)) / get_zone_total_orders(zone, total_orders)


def date_incrementer(date: datetime, time_step: timedelta):
    while True:
        date += time_step + timedelta(microseconds=lcg.randint(*TIME_DELTA_BETWEEN_STATUS))
        yield date


def random_possible_statuses(zone: dict):
    return lcg.choice(zone[ZONE_POSSIBLE_STATUSES_KEY])


# Combined fields
def generate_order_static_section() -> list:
    return [
        random_provider_id(PROVIDER_ID_LIST),
        random_direction(DIRECTION_LIST),
        random_tags(TAGS_LIST),
        random_description(),
        random_extra_data(lcg.randint(*RANDOM_EXTRA_DATA_HASH_RANGE))
    ]


def generate_order_dynamic_section(zone: dict, order_initial_date: datetime) -> list:
    dynamic_fields = []
    change_date = order_initial_date
    currency_pair = random_currency_pair(CURRENCY_PAIR_LIST)
    currency = currency_pair[CURRENCY_PAIR_NAME]
    px = currency_pair[CURRENCY_PAIR_VALUE]
    vol = random_vol(*RANDOM_VOL_RANGE)
    for status in random_possible_statuses(zone):
        if status != NEW_KEY:
            change_date += timedelta(microseconds=lcg.randint(*TIME_DELTA))
        if status == PARTIALLY_FILLED_KEY:
            px = round(lcg.randomly_modify_value(px, *PX_DELTA_RANGE), PX_DEFAULT_ROUND)
        if status == REJECTED_KEY:
            px = 0
            vol = 0
        dynamic_fields.append([str(change_date), status, currency, px, round(vol * px, VOL_DEFAULT_ROUND)])
    return dynamic_fields


order_id_sequence = iter(order_id_incrementer(get_initial_order_id_as_decimal(INITIAL_ORDER_ID)))


def generate_orders_for_zone(zone: dict):
    zone_orders = []
    order_id = next(order_id_sequence)
    order_creation_date = get_zone_initial_date(zone)
    date_sequence = iter(date_incrementer(get_zone_initial_date(zone), get_zone_time_step(zone, TOTAL_ORDERS)))
    for _ in range(get_zone_total_orders(zone, TOTAL_ORDERS)):
        order_static_section = generate_order_static_section()
        for dynamic_field in generate_order_dynamic_section(zone, order_creation_date):
            zone_orders.append([
                hex(order_id),
                *order_static_section,
                str(order_creation_date),
                *dynamic_field
            ])
        order_id = next(order_id_sequence)
        order_creation_date = next(date_sequence)
    return zone_orders


def generate_orders_for_all_zones():
    for zone in ZONES:
        result_list.append(generate_orders_for_zone(ZONES[zone]))


if __name__ == '__main__':
    logger.info('%s started' % APP_NAME)
    logger.info('start generating orders')

    try:
        generate_orders_for_all_zones()
    except Exception as e:
        logger.error(e, exc_info=EXCEPTION_INFO)
        sys.exit(1)
    else:
        logger.info('succsessfully generated %s zones' % len(result_list))

    logger.info('writing sql dump to %s' % sql_dump.name)
    try:
        for i in result_list:
            for j in i:
                sql_insert(sql_dump, TABLE_NAME, COLUMNS, j)
    except Exception as e:
        logger.exception(e, exc_info=EXCEPTION_INFO)
    else:
        logger.info('succsessfully wrote to %s' % sql_dump.name)
logger.info('Done')
