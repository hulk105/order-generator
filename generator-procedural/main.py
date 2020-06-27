from generators import *
from mylogging import logger
from myconfigparser import config

# DICT KEYS
FIRST_ENTRY = 'first_entry'
STEP = 'step'
MULTIPLIER = 'multiplier'
MAX_ENTRY = 'max_entry'
VALUES = 'values'

ITERATIONS = config['ITERATIONS'].get(int)

ORDERS = []

if __name__ == '__main__':
    # RED ZONE
    for i in range(300):
        # Get possible statuses randomly by random_index
        random_index = generate_random_number(
            config['STATUS']['red'][FIRST_ENTRY].get(int),
            config['STATUS']['red'][STEP].get(float),
            config['STATUS']['red'][MULTIPLIER].get(float),
            len(config['STATUS']['red'][VALUES].get()) - 1,
            i,
            round_result=True
        )
        POSSIBLE_STATUSES = config['STATUS']['red'][VALUES].get()[random_index]
        for status in POSSIBLE_STATUSES:
            # Order Id
            ORDER = [i, generate_order_id(
                config['ORDER_ID'][FIRST_ENTRY].get(int),
                config['ORDER_ID'][STEP].get(int),
                config['ORDER_ID'][MULTIPLIER].get(int),
                config['ORDER_ID'][MAX_ENTRY].get(int),
                i,
                # Provider Id
            ), generate_provider_id(
                config['PROVIDER_ID'][FIRST_ENTRY].get(int),
                config['PROVIDER_ID'][STEP].get(float),
                config['PROVIDER_ID'][MULTIPLIER].get(float),
                config['PROVIDER_ID'][MAX_ENTRY].get(int),
                i,
                config['PROVIDER_ID'][VALUES].get(),
                # Direction
            ), generate_direction(
                config['DIRECTION'][FIRST_ENTRY].get(int),
                config['DIRECTION'][STEP].get(float),
                config['DIRECTION'][MULTIPLIER].get(float),
                config['DIRECTION'][MAX_ENTRY].get(int),
                i,
                config['DIRECTION'][VALUES].get(),
                # Status
            ), status]

            # Append generated ORDER list to ORDERS
            ORDERS.append(ORDER)
            logger.info(ORDER)

# for order in ORDERS:
#     logger.info(order)

logger.info('Total orders generated: ' + str(len(ORDERS)))
