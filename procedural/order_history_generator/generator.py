import datetime
import hashlib
import gc

from pypika import Table, Query

import properties
import lcg_generator.generator as lcg
from logger import logger

orders_history = []
orders_table = Table('orders')
sql_dump_file = open('order_history_dump.sql', 'w')


def benchmark_function(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        logger.info('Finished in %s ms.' % str(end - start))
        return return_value

    return wrapper


@benchmark_function
def generate_order_history() -> None:
    for zone in properties.ZONES:
        generate_orders_for_zone(zone)


def show_total():
    logger.info('Total orders generated: %s' % str(len(orders_history)))


def generate_orders_for_zone(zone):
    logger.info('Generating orders for %s zone' % zone)

    # Log possible statuses
    logger.debug('Possible statuses for %s zone:' % zone)
    for statuses in properties.ZONES[zone][properties.statuses]:
        logger.debug(str(statuses))

    # Initial order_id
    order_id = properties.INITIAL_ORDER_ID

    # Parse Initial date
    creation_date = datetime.datetime.strptime(properties.ZONES[zone][properties.initial_date],
                                               properties.DATE_FORMAT)

    end_date = datetime.datetime.strptime(properties.ZONES[zone][properties.end_date],
                                          properties.DATE_FORMAT)

    # Time step for timedelta
    time_step = (end_date - creation_date) / properties.ZONES[zone][properties.orders_count]

    orders_in_zone_count = 0

    # Begin iterating
    for i in range(properties.ZONES[zone][properties.orders_count]):

        # Random Provider ID
        provider_id = lcg.choice(properties.PROVIDER_ID)

        # Random Direction
        direction = lcg.choice(properties.DIRECTION)

        # Random Currency Pair as a list ["CUR/CUR, 9.999999"]
        currency_pair = list(lcg.choice(properties.CURRENCY_PAIR).items())[0]

        # Initial Price
        px_init = currency_pair[1]

        # Random Price delta for each iteration
        px_delta = round(random_delta(0.000001, 0.00001, px_init), 6)

        # Random Vol
        vol = lcg.randfloat(1, 1000)

        # Random statuses from possible status list
        statuses = lcg.choice(properties.ZONES[zone][properties.statuses])

        # Initiate change date before status change
        change_date = creation_date

        # Generate random tags sample from tags list
        tags = lcg.sample(properties.TAGS, lcg.randint(1, 4))

        description = None

        extra_data = generate_extra_data(lcg.randint(1, 2000))

        # Changing status dependent fields
        for status in statuses:

            # TODO Nice hardcoded conditions
            if status != 'New':
                # Add random time delta (30s - 5m) for every new status if it is not New
                # TODO !!! This has to consider orders time dispersion for several thousands
                #  iterations, otherwise the date sequence in a single order will be invalid
                change_date += datetime.timedelta(microseconds=lcg.randint(30000000, 300000000))

            # Partially filled Price +- delta
            if status == 'Partially Filled':
                px_delta = round(random_delta(0.000001, 0.00001, px_init), 6)

            # Vol = 0 if status is Rejected
            if status == 'Rejected':
                vol = 0

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
            # Append to result List of orders
            orders_history.append(order)

            # Count order
            orders_in_zone_count += 1

        # Add random to these values up to next iteration
        order_id += lcg.randint(100, 600)
        # creation_date += datetime.timedelta(
        #     # 3,600 s * 1,000,000 μs * hours range in zone / orders count in zone + random (1 - 1,000,000 μs)
        #     microseconds=3600 * hour_range * 1000000 / properties.ORDERS_COUNT[zone] + lcg.randint(1, 100000)
        # )
        creation_date += time_step
    logger.info('DONE - Generated %s orders for %s zone' % (orders_in_zone_count, zone))


def random_delta(range_min, range_max, value):
    delta = lcg.randfloat(range_min, range_max)
    if lcg.randint(0, 1) == 0:
        return value + delta
    else:
        return value - delta


def generate_extra_data(*args):
    return hashlib.sha1(bytes(*args)).hexdigest()


@benchmark_function
def write_sql_dump():
    logger.info('Writing SQL dump to %s as %s' % (sql_dump_file.name, sql_dump_file.encoding))
    for order in orders_history:
        # Generate DB query
        query = Query.into(orders_table).insert(*order)
        sql_dump_file.write(str(query) + '\n')
