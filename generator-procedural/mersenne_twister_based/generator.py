import random
from mersenne_twister_based import settings
from custom_logger import setup_custom_logger

logger = setup_custom_logger(__name__)
random.seed(settings.SEED)
ORDERS = []


def random_sequence(first_entry, iterations, step_range_start, step_range_stop):
    count = 0
    result = []
    while count < iterations:
        result.append(first_entry)
        try:
            first_entry += random.randint(step_range_start, step_range_stop)
        except ValueError:
            return 'Error: empty range for random step range ' + str(step_range_start) + ' - ' + str(step_range_stop)
        count += 1

    return result


def generate_orders_by_mersenne_twister(zones):
    for zone in zones:
        generate_order_for_zone(zone)


def generate_order_for_zone(zone):
    logger.info('Generating orders for %s zone' % zone)
    logger.info('Possible statuses for %s zone:' % zone)
    for statuses in settings.POSSIBLE_STATUSES[zone]:
        logger.info(str(statuses))
