"""
Linear congruent sequence:
X_1 = (X * a + c) % m
X - first entry
a - coeff
c - step
m - max entry
"""

from mylogging import logger


def lcg(first_entry, step, multiplier, max_entry, iteration):
    count = 1
    if iteration < count:
        return first_entry
    else:
        next_entry = first_entry
        while count <= iteration:
            next_entry = (next_entry * multiplier + step) % max_entry
            count += 1
        return next_entry


def generate_random_number(first_entry, step, multiplier, max_entry, iteration, round_result=False):
    lcg_result = lcg(first_entry, step, multiplier, max_entry, iteration)
    if round_result is True:
        return round(lcg_result)
    else:
        return lcg_result


def generate_random_value_from_list(first_entry, step, multiplier, iteration, values, max_entry=0):
    max_entry = len(values) - 1
    lcg_result = lcg(first_entry, step, multiplier, max_entry, iteration)
    try:
        return values[round(lcg_result)]
    except IndexError as e:
        logger.error(e)


def generate_order_id(first_entry, step, multiplier, max_entry, iteration):
    lcg_result = lcg(first_entry, step, multiplier, max_entry, iteration)

    # Format to hex
    return format(round(lcg_result), 'x')


def generate_provider_id(first_entry, step, multiplier, max_entry, iteration, values):
    lcg_result = lcg(first_entry, step, multiplier, max_entry, iteration)

    # Get value by lcg generated index
    try:
        return values[round(lcg_result)]
    except IndexError as e:
        logger.error(e)


# SAME AS generate_provider_id
def generate_direction(first_entry, step, multiplier, max_entry, iteration, values):
    lcg_result = lcg(first_entry, step, multiplier, max_entry, iteration)

    # Get value by lcg generated index
    try:
        return values[round(lcg_result)]
    except IndexError as e:
        logger.error(e)


# TODO: Finish generator methods
def generate_currency_pair(status, iteration):
    pass


# TODO: Fix config variables
def generate_orders_lcg(zone, iterations):
    for i in range(iterations):
        # Get possible statuses randomly by random_index
        random_index = generate_random_number(
            first_entry=config[STATUS][zone][FIRST_ENTRY].get(int),
            step=config[STATUS][zone][STEP].get(float),
            multiplier=config[STATUS][zone][MULTIPLIER].get(float),
            max_entry=len(config[STATUS][zone][VALUES].get()) - 1,
            iteration=i,
            round_result=True
        )
        possible_statuses = config[STATUS][RED][VALUES].get()[random_index]
        order_partially_filled = False
        for status in possible_statuses:
            order_id = format(generate_random_number(
                first_entry=config[ORDER_ID][FIRST_ENTRY].get(int),
                step=config[ORDER_ID][STEP].get(float),
                multiplier=config[ORDER_ID][MULTIPLIER].get(float),
                max_entry=config[ORDER_ID][MAX_ENTRY].get(int),
                iteration=i,
                round_result=True
            ), 'x')
            provider_id = generate_random_value_from_list(
                first_entry=config[PROVIDER_ID][FIRST_ENTRY].get(int),
                step=config[PROVIDER_ID][STEP].get(float),
                multiplier=config[PROVIDER_ID][MULTIPLIER].get(float),
                iteration=i,
                values=config[PROVIDER_ID][VALUES].get(),
            )
            direction = generate_random_value_from_list(
                first_entry=config[DIRECTION][FIRST_ENTRY].get(int),
                step=config[DIRECTION][STEP].get(float),
                multiplier=config[DIRECTION][MULTIPLIER].get(float),
                iteration=i,
                values=config[DIRECTION][VALUES].get(),
            )
            currency_pair = list(generate_random_value_from_list(
                first_entry=config[CURRENCY_PAIR][FIRST_ENTRY].get(int),
                step=config[CURRENCY_PAIR][STEP].get(float),
                multiplier=config[CURRENCY_PAIR][MULTIPLIER].get(float),
                values=config[CURRENCY_PAIR][VALUES].get(),
                iteration=i,
            ).items())[0]
            currency_pair_delta = generate_random_number(
                first_entry=config[CURRENCY_PAIR]['delta'][FIRST_ENTRY].get(int),
                step=config[CURRENCY_PAIR]['delta'][STEP].get(float),
                multiplier=config[CURRENCY_PAIR]['delta'][MULTIPLIER].get(float),
                max_entry=config[CURRENCY_PAIR]['delta'][MAX_ENTRY].get(float),
                iteration=i,
            )
            currency_pair_delta_partially_filled = generate_random_number(
                first_entry=config[CURRENCY_PAIR]['delta_partially_filled'][FIRST_ENTRY].get(int),
                step=config[CURRENCY_PAIR]['delta_partially_filled'][STEP].get(float),
                multiplier=config[CURRENCY_PAIR]['delta_partially_filled'][MULTIPLIER].get(float),
                max_entry=config[CURRENCY_PAIR]['delta_partially_filled'][MAX_ENTRY].get(float),
                iteration=i,
            )
            price_volume_init = generate_random_number(
                first_entry=config[CURRENCY_PAIR]['px_vol'][FIRST_ENTRY].get(float),
                step=config[CURRENCY_PAIR]['px_vol'][STEP].get(float),
                multiplier=config[CURRENCY_PAIR]['px_vol'][MULTIPLIER].get(float),
                max_entry=config[CURRENCY_PAIR]['px_vol'][MAX_ENTRY].get(float),
                iteration=i,
            )
            currency_pair_currency = currency_pair[0]
            if order_partially_filled is not True and status == 'Partially Filled':
                currency_pair_value = round(currency_pair[1] + currency_pair_delta_partially_filled, 6)
                price_volume = round(currency_pair_value * price_volume_init, 6)
                order_partially_filled = True
            elif order_partially_filled is True:
                pass
            else:
                currency_pair_value = round(currency_pair[1] + currency_pair_delta, 6)
                price_volume = round(currency_pair_value * price_volume_init, 6)

            ORDER = [i, order_id, provider_id, direction, status, currency_pair_currency, currency_pair_value,
                     price_volume]

            # Append generated ORDER list to ORDERS
            ORDERS.append(ORDER)
            logger.info(ORDER)
