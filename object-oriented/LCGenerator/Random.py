from utils.utils import get_digits_count, get_decimal_hash

GOLDEN_RATIO = (1 + 5 ** 0.5) / 2
SEED_LENGTH = 8
DEFAULT_STEP_DIVIDER = 3
STEP_DIVIDER_LENGTH = 1
MULTIPLIER_INTEGER = 1
DEFAULT_MULTIPLIER = GOLDEN_RATIO


class LinearCongruentGenerator:
    def __init__(self, seed_value=None):
        self._seed = get_decimal_hash(seed_value, SEED_LENGTH)
        _seed_hash = get_decimal_hash(self._seed, SEED_LENGTH)
        self._step_divider = get_decimal_hash(self._seed, STEP_DIVIDER_LENGTH)
        self._multiplier = MULTIPLIER_INTEGER + (_seed_hash / (10 ** get_digits_count(_seed_hash)))
        self._sequence = iter(self._lcg(self._seed))

    def _lcg(self, max_value):
        current = self._seed
        step = max_value // self._step_divider
        while True:
            next_entry = (current * self._multiplier + step) % max_value
            yield next_entry
            current = next_entry

    @property
    def seed(self):
        """Change object instance seed parameters"""
        return self._seed

    @seed.setter
    def seed(self, seed_value):
        self._seed = get_decimal_hash(seed_value, SEED_LENGTH)

    def get_current_status(self):
        print(self._seed, self._step_divider, self._multiplier)

    def randint(self, min_value: int, max_value: int):
        result = round(next(self._sequence)) % (max_value + 1)
        if result < min_value:
            return result + min_value
        else:
            return result

    def randfloat(self, min_value: float, max_value: float):
        result = next(self._sequence) % max_value
        if result < min_value:
            return result + min_value
        else:
            return result

    def choice(self, population: list):
        result = round(next(self._sequence)) % len(population)
        return population[result]

    def sample(self, population: list, k: int):
        if k > len(population):
            raise ValueError('k is more than list length.')
        result_list = []
        for i in range(k):
            list_item = population[round(next(self._sequence)) % len(population)]
            result_list.append(list_item)
        return list(dict.fromkeys(result_list))

    def randomly_modify_value(self, range_min, range_max, value):
        delta = self.randfloat(range_min, range_max)
        if self.randint(0, 1) == 0:
            return value + delta
        else:
            return value - delta


random = LinearCongruentGenerator()
