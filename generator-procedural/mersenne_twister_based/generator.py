import random
import config as conf

random.seed(conf.SEED)


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


print(random_sequence(254781069873, 2000, 100, 1000))
