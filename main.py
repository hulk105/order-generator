from generators import *
from mylogging import logger
from myconfigparser import config

# DICT KEYS
first_entry = 'first_entry'
step = 'step'
multiplier = 'multiplier'
max_entries = 'max_entries'
values = 'values'

ORDERS = [[] for i in range(config.getint('CONSTANTS', 'ITERATIONS'))]

if __name__ == '__main__':
    for i in range(ITERATIONS):
        # Index
        ORDERS[i].append(i)

        # Order ID
        ORDERS[i].append(generate_order_id(
            config.getint('ORDER_ID', first_entry),
            config.getint('ORDER_ID', step),
            config.getint('ORDER_ID', multiplier),
            config.getint('ORDER_ID', max_entries),
            i,
        ))

        # Provider ID
        ORDERS[i].append(generate_provider_id(
            config.getint('PROVIDER_ID', first_entry),
            config.getfloat('PROVIDER_ID', step),
            config.getfloat('PROVIDER_ID', multiplier),
            config.getint('PROVIDER_ID', max_entries),
            i,
            config.get('PROVIDER_ID', values).split()
        ))


for order in ORDERS:
    logger.info(order)
