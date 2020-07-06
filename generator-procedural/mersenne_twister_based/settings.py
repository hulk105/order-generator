import sys
import logging
from config import config_parser

try:
    # Dictionary key strings
    FIRST_ENTRY = 'first_entry'
    STEP = 'step'
    MULTIPLIER = 'multiplier'
    MAX_ENTRY = 'max_entry'
    VALUES = 'values'
    STATUSES = 'statuses'
    orders_count = 'orders_count'

    # Categories strings
    ORDER_ID = 'ORDER_ID'
    CURRENCY_PAIR = 'CURRENCY_PAIR'

    ZONE = 'ZONE'
    RED = 'RED'
    GREEN = 'GREEN'
    BLUE = 'BLUE'

    # Constants
    SEED = config_parser['SEED'].get(int)
    INITIAL_ORDER_ID = config_parser['INITIAL_ORDER_ID'].get(int)
    PROVIDER_ID = config_parser['PROVIDER_ID'][VALUES].get()
    DIRECTION = config_parser['DIRECTION'][VALUES].get()
    ZONES = config_parser['ZONES'].get()

    POSSIBLE_STATUSES = {
        RED: ZONES[RED][STATUSES],
        GREEN: ZONES[GREEN][STATUSES],
        BLUE: ZONES[BLUE][STATUSES]
    }

    ORDERS_COUNT = {
        RED: ZONES[RED][orders_count],
        GREEN: ZONES[GREEN][orders_count],
        BLUE: ZONES[BLUE][orders_count]
    }


except KeyError as e:
    logging.critical('Key ' + str(e) + ' not specified in config')
    logging.warning('Exiting')
    sys.exit(1)
