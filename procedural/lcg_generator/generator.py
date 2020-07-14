import datetime
import itertools
import math
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
print('seed:', seed)

seed_as_float = seed
seed_size = get_digits_count(seed)

step_offset = get_digit(seed, 2)
if step_offset == 0 or step_offset == 1:
    step_offset = 3
print('step offset:', step_offset)

sequence_offset = get_digit(seed, 1)
print('seq offset:', sequence_offset)

while seed_size > 1:
    seed_as_float /= 10
    seed_size -= 1

print('seed:', seed)

multiplier = seed_as_float - int(seed_as_float) + 1
print('mul:', multiplier)


def lcg(min, max):
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


sequence = iter(lcg(0, seed))


def randint(min: int, max: int):
    result = round(next(itertools.islice(sequence, sequence_offset, None))) % (max + 1)
    if result < min:
        result += min
    return result


def choice(list: list):
    result = round(next(itertools.islice(sequence, sequence_offset, None))) % len(list)
    return list[result]
