from lcg_based.generator import *
from config import *
from decimal import *

getcontext().prec = 6

ORDERS = []


def generate_orders_mersenne_twister(zones):
    for zone in zones:
        generate_order_for_zone(zone)


def generate_order_for_zone(zone):
    logger.info('Start generating orders for %s zone' % zone)
    logger.info('Possible statuses for %s zone:' % zone)
    for statuses in POSSIBLE_STATUSES[zone]:
        logger.info(str(statuses))


if __name__ == '__main__':
    generate_orders_mersenne_twister(ZONES)

logger.info('Total orders generated: ' + str(len(ORDERS)))
