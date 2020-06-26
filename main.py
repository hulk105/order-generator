from generators import *
from mylogging import logger
from myconfigparser import config

# DICT KEYS
first_entry = 'first_entry'
step = 'step'
multiplier = 'multiplier'
max_entry = 'max_entry'
values = 'values'

ITERATIONS = config.getint('CONSTANTS', 'ITERATIONS')

ORDERS = [[] for i in range(ITERATIONS)]

if __name__ == '__main__':
    for i in range(ITERATIONS):
        # Index
        ORDERS[i].append(i)

        # Order ID
        ORDERS[i].append(generate_order_id(
            config.getint('ORDER_ID', first_entry),
            config.getint('ORDER_ID', step),
            config.getint('ORDER_ID', multiplier),
            config.getint('ORDER_ID', max_entry),
            i,
        ))

        # Provider ID
        ORDERS[i].append(generate_provider_id(
            config.getint('PROVIDER_ID', first_entry),
            config.getfloat('PROVIDER_ID', step),
            config.getfloat('PROVIDER_ID', multiplier),
            config.getint('PROVIDER_ID', max_entry),
            i,
            config.get('PROVIDER_ID', values).split()
        ))

        # Direction
        ORDERS[i].append(generate_provider_id(
            config.getint('DIRECTION', first_entry),
            config.getfloat('DIRECTION', step),
            config.getfloat('DIRECTION', multiplier),
            config.getint('DIRECTION', max_entry),
            i,
            config.get('DIRECTION', values).split()
        ))


for order in ORDERS:
    logger.info(order)
