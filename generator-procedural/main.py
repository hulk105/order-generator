from mersenne_twister_based import settings
from mersenne_twister_based.generator import generate_orders_by_mersenne_twister, orders
from custom_logger import setup_logger, setup_custom_logger
import logging

if __name__ == '__main__':
    setup_logger()
    logging.info('%s started', __name__)
    generate_orders_by_mersenne_twister(settings.ZONES)

    logging.info('Total orders generated: ' + str(len(orders)))
