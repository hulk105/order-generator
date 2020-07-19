import datetime
import hashlib
import logging
import math

import yaml

import constants as const


file = open(const.CONFIG_ABS_PATH)
config = yaml.load(file, Loader=yaml.FullLoader)

SEED = config['RANDOM_SEED']


def get_digit(number, n):
    return number // 10 ** n % 10


def get_digits_count(number):
    if number > 0:
        return int(math.log10(number)) + 1
    elif number == 0:
        return 1
    else:
        # +1 if you don't count the '-'
        return int(math.log10(-number)) + 2


def get_hash(value, length):
    return int(hashlib.sha1(str(value).encode('utf-8')).hexdigest(), 16) % (10 ** length)


if SEED is not None:
    seed = get_hash(SEED, 8)
    logging.debug('seed: %s' % SEED)
else:
    seed = get_hash(datetime.datetime.now().microsecond, 8)

logging.debug('seed hash: %s' % seed)

random_step = get_digit(seed, 2)
if random_step == 0 or random_step == 1:
    random_step = 3
logging.debug('random_step: %s' % random_step)

sequence_offset = get_digit(seed, 1)
logging.debug('sequence offset: %s' % sequence_offset)

seed_as_float = seed
seed_size = get_digits_count(seed)
while seed_size > 1:
    seed_as_float /= 10
    seed_size -= 1
logging.debug('seed float %s' % seed_as_float)

multiplier = seed_as_float - int(seed_as_float) + 1
logging.debug('multiplier: %s' % multiplier)


def lcg(max):
    current = seed
    step = max // random_step
    logging.debug('Step: %s' % step)
    while True:
        next = (current * multiplier + step) % max
        yield next
        current = next


sequence = iter(lcg(seed))


def randint(min: int, max: int):
    result = round(next(sequence)) % (max + 1)
    if result < min:
        return result + min
    else:
        return result


def randfloat(min: float, max: float):
    result = next(sequence) % max
    if result < min:
        return result + min
    else:
        return result


def choice(population: list):
    result = round(next(sequence)) % len(population)
    return population[result]


def sample(population: list, k: int):
    if k > len(population):
        raise ValueError('k is more than list length.')
    result_list = []
    for i in range(k):
        list_item = population[round(next(sequence)) % len(population)]
        result_list.append(list_item)
    return list(dict.fromkeys(result_list))


def randomly_modify_value(range_min, range_max, value):
    delta = randfloat(range_min, range_max)
    if randint(0, 1) == 0:
        return value + delta
    else:
        return value - delta
