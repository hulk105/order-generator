import datetime
import itertools
import math
import traceback

from config_parser import config_parser
import properties


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


if properties.SEED is not None:
    seed = properties.SEED
else:
    seed = datetime.datetime.now().microsecond

seed_float = seed

seed_size = get_digits_count(seed)
print('seed:', seed)

step_offset = get_digit(seed, 2)
if step_offset == 0 or step_offset == 1:
    step_offset = 3
print('step offset:', step_offset)

sequence_offset = get_digit(seed, 1)
print('seq offset:', sequence_offset)

while seed_size > 1:
    seed_float /= 10
    seed_size -= 1

print('seed:', seed)

multiplier = seed_float - int(seed_float) + 1
print('mul:', multiplier)


sequence = {}


def lcg(min, max, first=None):
    current = min
    step = (min + max) / step_offset
    print('Step:', step)
    while True:
        next = (current * multiplier + step) % max
        if next < min:
            yield next + min
        else:
            yield next
        current = next


def initiate_sequence(*args):
    sequence[len(sequence) + 1] = (iter(lcg(*args)))
    return len(sequence) + 1, iter(lcg(*args))


def randint(min: int, max: int, first=None):
    global sequence
    if sequence is None:
        sequence = iter(lcg(min, max))
        return round(next(itertools.islice(sequence, sequence_offset, None)))
    else:
        return round(next(sequence))


def choice(list: list):
    global sequence
    if sequence is None:
        sequence.append(iter(lcg(0, len(list) - 1)))
        return list[round(next(itertools.islice(sequence, sequence_offset, None)))]
    else:
        return list[round(next(sequence))]


# for _ in range(100):
#     print(randint(0, 1), randint(100, 1000), choice(['SQM', 'FXCM']), choice(['Buy', 'Sell']))

for _ in range(5):
    print(id(get_digits_count(123)))
    print(id(get_digits_count(12)))

