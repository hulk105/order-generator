import sys

from config import config_parser
from custom_logger import setup_custom_logger

logger = setup_custom_logger(__name__)

try:
    # Dictionary key strings
    FIRST_ENTRY = 'first_entry'
    STEP = 'step'
    MULTIPLIER = 'multiplier'
    MAX_ENTRY = 'max_entry'
    VALUES = 'values'
    STATUSES = 'statuses'

    # Categories strings
    ORDER_ID = 'ORDER_ID'
    PROVIDER_ID = 'PROVIDER_ID'
    DIRECTION = 'DIRECTION'
    CURRENCY_PAIR = 'CURRENCY_PAIR'

    ZONE = 'ZONE'
    RED = 'RED'
    GREEN = 'GREEN'
    BLUE = 'BLUE'

    # Constants
    ITERATIONS = config_parser['ITERATIONS'].get(int)

    SEED = config_parser['SEED'].get(int)

    ZONES = config_parser['ZONES'].get()

    POSSIBLE_STATUSES = {
        RED: ZONES[RED][STATUSES],
        GREEN: ZONES[GREEN][STATUSES],
        BLUE: ZONES[BLUE][STATUSES]
    }
except KeyError as e:
    logger.critical('Key ' + str(e) + ' not specified in config')
    logger.warning('Exiting')
    sys.exit(1)
