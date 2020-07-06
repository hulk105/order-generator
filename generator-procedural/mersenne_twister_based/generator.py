import math
import random
from mersenne_twister_based import settings
import logging

random.seed(settings.SEED)

orders = []


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
        generate_orders_for_zone(zone)


def generate_orders_for_zone(zone):
    # Initial
    order_id = settings.INITIAL_ORDER_ID
    logging.info('Generating orders for %s zone' % zone)
    logging.debug('Possible statuses for %s zone:' % zone)
    for statuses in settings.POSSIBLE_STATUSES[zone]:
        logging.debug(str(statuses))

    for i in range(settings.ORDERS_COUNT[zone]):
        logging.debug(i)
        logging.debug(order_id)

        # provider_id = random.choice(settings.PROVIDER_ID)
        if random.randint(0, 1000) % 2 == 0:
            provider_id = settings.PROVIDER_ID[0]
        else:
            provider_id = settings.PROVIDER_ID[1]

        # Get random statuses from status list
        statuses = random.choice(settings.POSSIBLE_STATUSES[zone])
        for status in statuses:
            logging.debug(status)
            order = [
                i,
                hex(order_id),
                provider_id,
                status
            ]
            logging.info(order)
            orders.append(order)
        order_id += random.randint(100, 600)
