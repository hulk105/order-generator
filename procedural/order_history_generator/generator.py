from datetime import timedelta, datetime
from hashlib import sha1

import constants as const
import lcg_generator.random as lcg

# Dictionary key strings
POSSIBLE_STATUSES = 'possible_statuses'
PERCENT_OF_TOTAL_ORDERS = 'percent_of_total_orders'
INITIAL_DATE = 'initial_date'
END_DATE = 'end_date'
DELTA = 'delta'
ZONES = 'ZONES'
TOTAL_ORDERS = 'TOTAL_ORDERS'
INITIAL_ORDER_ID = 'INITIAL_ORDER_ID'
PROVIDER_ID = 'PROVIDER_ID'
DIRECTION = 'DIRECTION'
CURRENCY_PAIR = 'CURRENCY_PAIR'
CURRENCY_PAIR_NAME = 0
CURRENCY_PAIR_VALUE = 1
TAGS = 'TAGS'
ORDER_ID_INCREMENT_RANGE = 3, 10
PX_DEFAULT_ROUND = 6
PX_DELTA_RANGE = 0.000001, 0.00001
VOL_DEFAULT_ROUND = 4
NUMBER_OF_TAGS_PER_ORDER = 1, 2
RANDOM_VOL_RANGE = 1, 1000
RANDOM_EXTRA_DATA_HASH_RANGE = 1, 2000

# 30-60 seconds as microseconds
TIME_DELTA = 30000000, 60000000


def generate_orders_history(data: dict, result_list: list):
    # Incremental fields
    def get_initial_order_id():
        initial_order_id = int(data[INITIAL_ORDER_ID], 16)
        return initial_order_id

    def increment_order_id():
        order_id = get_initial_order_id()
        while True:
            order_id += lcg.randint(*ORDER_ID_INCREMENT_RANGE)
            yield order_id

    def random_provider_id():
        provider_id = lcg.choice(data[PROVIDER_ID])
        return provider_id

    def random_direction():
        direction = lcg.choice(data[DIRECTION])
        return direction

    def random_currency_pair():
        currency_pair = lcg.choice(list(data[CURRENCY_PAIR].items()))
        currency = currency_pair[CURRENCY_PAIR_NAME]
        px_init = currency_pair[CURRENCY_PAIR_VALUE]
        px = round(lcg.randomly_modify_value(*PX_DELTA_RANGE, px_init), PX_DEFAULT_ROUND)
        return [currency, px]

    def random_vol():
        vol = lcg.randint(*RANDOM_VOL_RANGE)
        return vol

    def random_tags():
        tags = lcg.sample(data[TAGS], lcg.randint(*NUMBER_OF_TAGS_PER_ORDER))
        return tags

    def random_description():
        pass
        return None

    def random_extra_data():
        extra_data = lcg.randint(*RANDOM_EXTRA_DATA_HASH_RANGE)
        return sha1(bytes(extra_data)).hexdigest()

    # Dynamic (zone specific) fields
    def get_zone_orders_count(zone):
        total_orders = data[TOTAL_ORDERS]
        percent_of_total_orders = data[ZONES][zone][PERCENT_OF_TOTAL_ORDERS]
        zone_orders_count = int(total_orders * percent_of_total_orders)
        return zone_orders_count

    def get_zone_initial_date(zone):
        creation_date = datetime.strptime(data[ZONES][zone][INITIAL_DATE], const.DEFAULT_DATE_FORMAT)
        return creation_date

    def get_zone_end_date(zone):
        end_date = datetime.strptime(data[ZONES][zone][END_DATE], const.DEFAULT_DATE_FORMAT)
        return end_date

    def get_zone_time_step(zone):
        time_step = (get_zone_end_date(zone) - get_zone_initial_date(zone)) / get_zone_orders_count(zone)
        return time_step

    def increment_date(zone):
        date = get_zone_initial_date(zone)
        time_step = get_zone_time_step(zone)
        while True:
            date += time_step + timedelta(microseconds=lcg.randint(100, 999999))
            yield date

    def random_possible_statuses(zone):
        statuses = lcg.choice(data[ZONES][zone][POSSIBLE_STATUSES])
        return statuses

    # Combined fields
    def generate_order_static_section() -> list:
        return [
            random_provider_id(),
            random_direction(),
            random_tags(),
            random_description(),
            random_extra_data(),
        ]

    def generate_order_dynamic_section(zone, initial_date: datetime) -> list:
        possible_statuses = random_possible_statuses(zone)
        change_date = initial_date
        currency_pair = random_currency_pair()
        currency_name = currency_pair[CURRENCY_PAIR_NAME]
        px = currency_pair[CURRENCY_PAIR_VALUE]
        vol = random_vol()
        dynamic_fields = []
        for status in possible_statuses:
            if status != 'New':
                change_date += timedelta(microseconds=lcg.randint(*TIME_DELTA))
            if status == 'Partially Filled':
                px = round(lcg.randomly_modify_value(*PX_DELTA_RANGE, px), PX_DEFAULT_ROUND)
            if status == 'Rejected':
                px = 0
                vol = 0
            dynamic_fields.append(
                [str(change_date), status, currency_name, px, round(vol * px, VOL_DEFAULT_ROUND)]
            )
        return dynamic_fields

    order_id_sequence = iter(increment_order_id())

    def generate_orders_for_zone(zone):
        zone_orders = []
        date_sequence = iter(increment_date(zone))
        order_creation_date = next(date_sequence)
        for _ in range(get_zone_orders_count(zone)):
            for dynamic_field in generate_order_dynamic_section(zone, order_creation_date):
                zone_orders.append([
                    hex(next(order_id_sequence)),
                    *generate_order_static_section(),
                    str(order_creation_date),
                    *dynamic_field
                ])
            order_creation_date = next(date_sequence)
        return zone_orders

    def generate_orders_for_all_zones():
        for zone in data[ZONES]:
            result_list.append(generate_orders_for_zone(zone))

    return generate_orders_for_all_zones()
