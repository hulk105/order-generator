"""
Confuse searches for config.yaml at /home/user/.config/<APP_NAME>
"""

import confuse

APP_NAME = 'order-generator-procedural'

config_parser = confuse.Configuration(APP_NAME)

# Logging
LOGGING_LEVEL = config_parser['LOG_LEVEL'].get()

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
