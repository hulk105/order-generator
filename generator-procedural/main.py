from mersenne_twister_based import settings
from mersenne_twister_based.generator import generate_orders_by_mersenne_twister, ORDERS
from custom_logger import setup_custom_logger

if __name__ == '__main__':
    generate_orders_by_mersenne_twister(settings.ZONES)

    setup_custom_logger(__name__).info('Total orders generated: ' + str(len(ORDERS)))
