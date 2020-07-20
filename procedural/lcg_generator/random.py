from datetime import datetime

import yaml

from utils.utils import get_decimal_hash, get_digits_count
import constants as const

file = open(const.CONFIG_ABS_PATH)
config = yaml.load(file, Loader=yaml.FullLoader)

RANDOM_SEED = 'RANDOM_SEED'
SEED = config[RANDOM_SEED]
DEFAULT_SEED_LENGTH = 8
DEFAULT_STEP_DIVIDER = 3
STEP_DIVIDER_LENGTH = 1
MULTIPLIER_INTEGER = 1

seed = get_decimal_hash(SEED, DEFAULT_SEED_LENGTH) \
    if SEED is not None \
    else get_decimal_hash(datetime.now().microsecond, 8)

seed_hash = get_decimal_hash(seed, DEFAULT_SEED_LENGTH)

step_divider = DEFAULT_STEP_DIVIDER \
    if get_decimal_hash(seed, STEP_DIVIDER_LENGTH) == 0 \
    else get_decimal_hash(seed, STEP_DIVIDER_LENGTH)

multiplier = MULTIPLIER_INTEGER + seed_hash / (10 ** get_digits_count(seed_hash))


def lcg(max):
    current = seed
    step = max // step_divider
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
