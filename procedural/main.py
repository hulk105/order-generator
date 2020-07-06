from mersenne_twister_based import settings
from mersenne_twister_based.generator import generate_order_history, orders
from config import setup_logger
import logging

if __name__ == '__main__':
    setup_logger()
    logging.info('%s started', __name__)
    total = generate_order_history(settings.ZONES)

    logging.info('Total orders generated: ' + str(len(orders)))