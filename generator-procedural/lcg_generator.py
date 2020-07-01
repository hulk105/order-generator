"""
Linear congruent sequence:
X_1 = (X * a + c) % m
X - first entry
a - coeff
c - step
m - max entry
549755813887 = 7FFFFFFFFF
"""

from mylogging import logger
import random
import constants as const

random.seed(const.SEED)


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


def generate_currency_pair(status, iteration):
    pass
