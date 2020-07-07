from mersenne_twister_based import generator_properties
from mersenne_twister_based.generator import generate_order_history, orders_history
from logger import logger

if __name__ == '__main__':
    logger.info('%s started', __name__)
    generate_order_history(generator_properties.ZONES)
    logger.info('Total orders generated: ' + str(len(orders_history)))
