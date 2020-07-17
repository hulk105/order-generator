import datetime
import hashlib
import logging

import yaml
from pypika import Table, Query

import constants as const
import lcg_generator.generator as lcg

# Dictionary key strings
POSSIBLE_STATUSES = 'possible_statuses'
PERCENT_OF_TOTAL_ORDERS = 'percent_of_total_orders'
INITIAL_DATE = 'initial_date'
END_DATE = 'end_date'
DELTA = 'delta'
ZONES = 'ZONES'
TOTAL_ORDERS = 'TOTAL_ORDERS'
INITIAL_ORDER_ID = 'INITIAL_ORDER_ID'
ORDER_ID_INCREMENT = 3, 10
PROVIDER_ID = 'PROVIDER_ID'
DIRECTION = 'DIRECTION'
CURRENCY_PAIR = 'CURRENCY_PAIR'
PX_DEFAULT_ROUND = 6
PX_DELTA = 0.000001, 0.00001
VOL_DEFAULT_ROUND = 4
TAGS = 'TAGS'
TAGS_PER_ORDER = 1, 2
TIME_DELTA = 30000000, 60000000

orders = []
orders_history = []


def get_config(path):
    config_file = open(path)
    return yaml.load(config_file, Loader=yaml.FullLoader)


config = get_config(const.CONFIG_PATH)


def benchmark_function(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        logging.info('Finished in %s seconds' % str(end - start))
        return return_value

    return wrapper


def add_up_random_float_to_value(range_min, range_max, value):
    delta = lcg.randfloat(range_min, range_max)
    if lcg.randint(0, 1) == 0:
        return value + delta
    else:
        return value - delta


def get_initial_order_id():
    initial_order_id = int(config[INITIAL_ORDER_ID], 16)
    return initial_order_id


def random_provider_id():
    provider_id = lcg.choice(config[PROVIDER_ID])
    return provider_id


def random_direction():
    direction = lcg.choice(config[DIRECTION])
    return direction


def random_currency_pair():
    currency_pair = lcg.choice(list(config[CURRENCY_PAIR].items()))
    currency_pair_string = currency_pair[0]
    px_init = currency_pair[1]
    px = round(add_up_random_float_to_value(*PX_DELTA, px_init), PX_DEFAULT_ROUND)
    return [currency_pair_string, px]


def random_vol():
    vol = lcg.randint(1, 1000)
    return vol


def random_tags():
    tags = lcg.sample(config[TAGS], lcg.randint(*TAGS_PER_ORDER))
    return tags


def random_description():
    pass
    return None


def random_extra_data():
    extra_data = lcg.randint(1, 2000)
    return hashlib.sha1(bytes(extra_data)).hexdigest()


# Zone specific fields
def get_zone_orders_count(zone):
    total_orders = config[TOTAL_ORDERS]
    percent_of_total_orders = config[ZONES][zone][PERCENT_OF_TOTAL_ORDERS]
    zone_orders_count = int(total_orders * percent_of_total_orders)
    logging.debug('Orders to generate: %s' % zone_orders_count)
    return zone_orders_count


def get_zone_initial_date(zone):
    creation_date = datetime.datetime.strptime(config[ZONES][zone][INITIAL_DATE], const.DEFAULT_DATE_FORMAT)
    return creation_date


def get_zone_end_date(zone):
    end_date = datetime.datetime.strptime(config[ZONES][zone][END_DATE], const.DEFAULT_DATE_FORMAT)
    return end_date


def get_zone_time_step(zone):
    time_step = (get_zone_end_date(zone) - get_zone_initial_date(zone)) / get_zone_orders_count(zone)
    return time_step


def random_possible_statuses(zone):
    statuses = lcg.choice(config[ZONES][zone][POSSIBLE_STATUSES])
    return statuses


def generate_orders_for_zone(zone):
    logging.info('Generating orders for %s zone' % zone)
    order_id = get_initial_order_id()
    creation_date = get_zone_initial_date(zone)
    time_step = get_zone_time_step(zone)
    for i in range(get_zone_orders_count(zone)):
        for dynamic_field in generate_order_dynamic_section(zone, creation_date):
            orders.append([
                hex(order_id),
                str(creation_date),
                generate_order_static_section(),
                dynamic_field
            ])
        order_id += lcg.randint(*ORDER_ID_INCREMENT)
        creation_date += time_step


def generate_order_static_section():
    return [
        random_provider_id(),
        random_direction(),
        random_tags(),
        random_description(),
        random_extra_data(),
    ]


def generate_order_dynamic_section(zone, creation_date: datetime):
    possible_statuses = random_possible_statuses(zone)
    change_date = creation_date
    currency_pair = random_currency_pair()
    currency = currency_pair[0]
    px = currency_pair[1]
    vol = random_vol()
    dynamic_fields = []
    for status in possible_statuses:
        if status != 'New':
            change_date += datetime.timedelta(microseconds=lcg.randint(*TIME_DELTA))
        if status == 'Partially Filled':
            px = round(add_up_random_float_to_value(*PX_DELTA, px), PX_DEFAULT_ROUND)
        if status == 'Rejected':
            px = 0
            vol = 0
        dynamic_fields.append([status, str(change_date), currency, px,
                               round(vol * px, VOL_DEFAULT_ROUND)])
    return dynamic_fields


@benchmark_function
def write_sql_dump():
    orders_table = Table(const.TABLE_NAME)
    sql_dump_file = open(const.SQL_DUMP_FILENAME, 'w')
    logging.info('Writing SQL dump to %s as %s' % (sql_dump_file.name, sql_dump_file.encoding))
    for order in orders_history:
        # Generate DB query
        query = Query.into(orders_table).insert(*order)
        sql_dump_file.write(str(query) + '\n')


def show_total():
    logging.info('Total orders with statuses generated: %s' % str(len(orders_history)))


generate_orders_for_zone('GREEN')
for order in orders:
    print(order)
