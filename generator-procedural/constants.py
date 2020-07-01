from myconfigparser import config

CONFIG_FOLDER = 'order-generator-procedural'

# Dictionary keys
FIRST_ENTRY = 'first_entry'
STEP = 'step'
MULTIPLIER = 'multiplier'
MAX_ENTRY = 'max_entry'
VALUES = 'values'
ORDER_ID = 'ORDER_ID'
PROVIDER_ID = 'PROVIDER_ID'
DIRECTION = 'DIRECTION'
CURRENCY_PAIR = 'CURRENCY_PAIR'
STATUS = 'STATUS'
RED = 'RED'
GREEN = 'GREEN'
BLUE = 'BLUE'

SEED = config['SEED'].get(int)
ITERATIONS = config['ITERATIONS'].get(int)

POSSIBLE_STATUSES = config[STATUS][RED][VALUES].get(), \
                    config[STATUS][GREEN][VALUES].get(), \
                    config[STATUS][BLUE][VALUES].get()
