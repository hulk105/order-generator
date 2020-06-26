from generators import *
from mylogging import logger
from myconfigparser import config

# DICT KEYS
first_entry = 'first_entry'
step = 'step'
multiplier = 'multiplier'
max_entry = 'max_entry'
values = 'values'

ITERATIONS = config['ITERATIONS'].get(int)

ORDERS = [[] for i in range(ITERATIONS)]

if __name__ == '__main__':
    for i in range(ITERATIONS):
        # Index
        ORDERS[i].append(i)

        # Order ID
        ORDERS[i].append(generate_order_id(
            config['ORDER_ID'][first_entry].get(int),
            config['ORDER_ID'][step].get(int),
            config['ORDER_ID'][multiplier].get(int),
            config['ORDER_ID'][max_entry].get(int),
            i,
        ))

        # Provider ID
        ORDERS[i].append(generate_provider_id(
            config['PROVIDER_ID'][first_entry].get(int),
            config['PROVIDER_ID'][step].get(float),
            config['PROVIDER_ID'][multiplier].get(float),
            config['PROVIDER_ID'][max_entry].get(int),
            i,
            config['PROVIDER_ID'][values].get(),
        ))

        # Direction
        ORDERS[i].append(generate_provider_id(
            config['DIRECTION'][first_entry].get(int),
            config['DIRECTION'][step].get(float),
            config['DIRECTION'][multiplier].get(float),
            config['DIRECTION'][max_entry].get(int),
            i,
            config['DIRECTION'][values].get(),
        ))


for order in ORDERS:
    logger.info(order)
