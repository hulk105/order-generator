'''
first_entry - first entry
multiplier - coeff
step - step
max_entry - max entry
549755813887 = 7FFFFFFFFF
'''

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


def generate_order_id(first_entry, step, multiplier, max_entry, iteration):
    lcg_result = lcg(first_entry, step, multiplier, max_entry, iteration)

    # Format to hex
    return format(lcg_result, 'x')


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
