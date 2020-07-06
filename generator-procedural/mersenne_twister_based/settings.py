import sys
import logging

from config import config_parser

try:
    # Dictionary key strings
    values = 'values'
    statuses = 'statuses'
    orders_count = 'orders_count'
    initial_date = 'initial_date'
    delta = 'delta'

    # Categories strings
    ORDER_ID = 'ORDER_ID'

    ZONE = 'ZONE'
    RED = 'RED'
    GREEN = 'GREEN'
    BLUE = 'BLUE'

    # Constants
    SEED = config_parser['SEED'].get(int)

    ZONES = config_parser['ZONES'].get()

    POSSIBLE_STATUSES = {
        RED: ZONES[RED][statuses],
        GREEN: ZONES[GREEN][statuses],
        BLUE: ZONES[BLUE][statuses]
    }

    ORDERS_COUNT = {
        RED: ZONES[RED][orders_count],
        GREEN: ZONES[GREEN][orders_count],
        BLUE: ZONES[BLUE][orders_count]
    }

    INITIAL_DATE = {
        RED: ZONES[RED][initial_date],
        GREEN: ZONES[GREEN][initial_date],
        BLUE: ZONES[BLUE][initial_date]
    }

    DATE_FORMAT = '%Y-%m-%d %H:%M:%S.%f'

    INITIAL_ORDER_ID = config_parser['INITIAL_ORDER_ID'].get(int)
    PROVIDER_ID = config_parser['PROVIDER_ID'][values].get()
    DIRECTION = config_parser['DIRECTION'][values].get()
    CURRENCY_PAIR = config_parser['CURRENCY_PAIR'][values].get()
    CURRENCY_PAIR_DELTA = config_parser['CURRENCY_PAIR'][delta].get(float)


except KeyError as e:
    logging.critical('Key ' + str(e) + ' not specified in config')
    logging.warning('Exiting')
    sys.exit(1)
