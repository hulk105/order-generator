import datetime
import logging
import random
import hashlib

from mersenne_twister_based import settings

random.seed(settings.SEED)
orders = []


def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        logging.info('Finished in: %s ms.' % str(end - start))
        return return_value
    return wrapper


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


@benchmark
def generate_order_history(zones):
    for zone in zones:
        generate_orders_for_zone(zone)


def generate_orders_for_zone(zone):

    # Initial order_id
    order_id = settings.INITIAL_ORDER_ID

    # Initial date
    creation_date = datetime.datetime.strptime(settings.INITIAL_DATE[zone], settings.DATE_FORMAT)
    hour_range = 23 - creation_date.hour

    # Log possible statuses for zone
    logging.info('Generating orders for %s zone' % zone)
    logging.debug('Possible statuses for %s zone:' % zone)
    for statuses in settings.POSSIBLE_STATUSES[zone]:
        logging.debug(str(statuses))

    # Begin iterating
    logging.debug('Iterating')
    for i in range(settings.ORDERS_COUNT[zone]):
        logging.debug('Iteration %s:' % str(i))
        logging.debug('Order ID %s:' % str(order_id))

        # Random Provider ID
        provider_id = random.choice(settings.PROVIDER_ID)

        # Random Direction
        direction = random.choice(settings.DIRECTION)

        # Random Currency Pair as a list ["CUR/CUR, 9.999999"]
        currency_pair = list(random.choice(settings.CURRENCY_PAIR).items())[0]
        logging.debug('Currency pair: %s' % str(currency_pair))

        # Initial Price
        px_init = currency_pair[1]

        # Random Price delta for each iteration
        delta = random.triangular(0.000001, 0.00001)
        if random.randint(0, 1) == 0:
            px_delta = round(px_init + delta, 6)
            logging.debug('%s + %s = %s' % (px_init, delta, px_delta))
        else:
            px_delta = round(px_init - delta, 6)
            logging.debug('%s + %s = %s' % (px_init, delta, px_delta))

        # Random Vol
        vol = random.randint(1, 1000) + random.random()

        # Random statuses from possible status list
        statuses = random.choice(settings.POSSIBLE_STATUSES[zone])

        # Initiate change date before status change
        change_date = creation_date

        # Generate random tags sample from tags list
        tags = random.sample(settings.TAGS, random.randint(1, 4))

        description = None

        extra_data = hashlib.sha1(bytes(random.getrandbits(i + 1))).hexdigest()

        # Changing status dependent fields
        for status in statuses:
            logging.debug(status)

            # Partially filled Price delta
            if status == 'Partially Filled':
                if random.randint(0, 1) == 0:
                    px_delta = round(px_init + delta, 6)
                    logging.debug('%s + %s = %s' % (px_init, delta, px_delta))
                else:
                    px_delta = round(px_init - delta, 6)
                    logging.debug('%s + %s = %s' % (px_init, delta, px_delta))

            # Vol = 0 if status is Rejected
            if status == 'Rejected':
                vol = 0

            if status != 'New':
                # Add random time delta (30s - 5m) for every new status if not New
                change_date += datetime.timedelta(microseconds=random.randint(30000000, 300000000))

            # Result Order
            order = [
                i,
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
            logging.info(order)

            # Append to result List of orders
            orders.append(order)

        # Add random to these values up to next iteration
        order_id += random.randint(100, 600)
        creation_date += datetime.timedelta(
            microseconds=3600000000*hour_range/settings.ORDERS_COUNT[zone]+random.randint(1, 1000000)
        )
