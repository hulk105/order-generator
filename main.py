import logging
import configparser
from generators import *

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

config = configparser.ConfigParser()
config.read('config.ini')

# DICT KEYS
first_entry = 'first_entry'
step = 'step'
multiplier = 'multiplier'
max_entries = 'max_entries'

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

for order in ORDERS:
    logger.info(order)
