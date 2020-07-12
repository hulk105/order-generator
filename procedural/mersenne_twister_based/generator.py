import datetime
import hashlib
import random

from pypika import Table, Query

import properties
from logger import logger

orders_history = []
orders_table = Table('orders')
sql_dump = open('order_history_dump.sql', 'w')


def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        logger.info('Finished in: %s ms.' % str(end - start))
        return return_value

    return wrapper


def set_random_seed() -> None:
    if properties.SEED is not None:
        random.seed(properties.SEED)
        logger.info('Random seed: %s' % properties.SEED)
    else:
        logger.warning('Random seed not specified, using current datetime microseconds')


@benchmark
def generate_order_history() -> None:
    for zone in properties.ZONES:
        generate_orders_for_zone(zone)


def show_total():
    logger.info('Total orders generated: %s' % str(len(orders_history)))


def generate_orders_for_zone(zone):
    # Log possible statuses for zone
    logger.info('Generating orders for %s zone' % zone)
    logger.debug('Possible statuses for %s zone:' % zone)
    for statuses in properties.POSSIBLE_STATUSES[zone]:
        logger.debug(str(statuses))

    # Initial order_id
    order_id = properties.INITIAL_ORDER_ID

    # Parse Initial date
    creation_date = datetime.datetime.strptime(properties.INITIAL_DATE[zone],
                                               properties.DATE_FORMAT)
    # Hour range for timedelta
    hour_range = 23 - creation_date.hour

    orders_in_zone_count = 0

    # Begin iterating
    logger.debug('Iterating')
    for i in range(properties.ORDERS_COUNT[zone]):
        logger.debug('Iteration %s:' % str(i))
        logger.debug('Order ID %s' % str(order_id))

        # Random Provider ID
        provider_id = random.choice(properties.PROVIDER_ID)

        # Random Direction
        direction = random.choice(properties.DIRECTION)

        # Random Currency Pair as a list ["CUR/CUR, 9.999999"]
        currency_pair = list(random.choice(properties.CURRENCY_PAIR).items())[0]
        logger.debug('Currency pair: %s' % str(currency_pair))

        # Initial Price
        px_init = currency_pair[1]

        # Random Price delta for each iteration
        px_delta = round(random_delta(0.000001, 0.00001, px_init), 6)

        # Random Vol
        vol = random.randint(1, 1000) + random.random()

        # Random statuses from possible status list
        statuses = random.choice(properties.POSSIBLE_STATUSES[zone])

        # Initiate change date before status change
        change_date = creation_date

        # Generate random tags sample from tags list
        tags = random.sample(properties.TAGS, random.randint(1, 4))

        description = None

        extra_data = generate_extra_data(random.randint(1, 2000))

        # Changing status dependent fields
        for status in statuses:
            logger.debug('Status: %s' % status)

            # Partially filled Price delta
            if status == 'Partially Filled':
                px_delta = round(random_delta(0.000001, 0.00001, px_init), 6)

            # Vol = 0 if status is Rejected
            if status == 'Rejected':
                vol = 0

            if status != 'New':
                # Add random time delta (30s - 5m) for every new status if not New
                change_date += datetime.timedelta(microseconds=random.randint(30000000, 300000000))

            # Result Order
            order = [
                hex(order_id),
                provider_id,
                direction,
                currency_pair[0],
                px_delta,
                round(vol * px_delta, 6),
                str(creation_date),
                str(change_date),
                status,
                tags,
                description,
                extra_data
            ]
            logger.debug(order)

            # Append to result List of orders
            orders_history.append(order)

            orders_in_zone_count += 1

            # Generate DB query
            query = Query.into(orders_table).insert(*order)
            logger.debug(query)
            sql_dump.write(str(query) + '\n')

        # Add random to these values up to next iteration
        order_id += random.randint(100, 600)
        creation_date += datetime.timedelta(
            # 3,600 s * 1,000,000 μs * hours range in zone / orders count in zone + random (1 - 1,000,000 μs)
            microseconds=3600 * 1000000 * hour_range / properties.ORDERS_COUNT[zone] + random.randint(1,
                                                                                                      100000)
        )
    logger.info('DONE - Generated %s orders for %s zone' % (orders_in_zone_count, zone))


def random_delta(range_min, range_max, value):
    delta = random.triangular(range_min, range_max)
    if random.randint(0, 1) == 0:
        return value + delta
    else:
        return value - delta


def generate_extra_data(*args):
    return hashlib.sha1(bytes(*args)).hexdigest()
