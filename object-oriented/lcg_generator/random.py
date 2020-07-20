import math

from utils.utils import get_digits_count, get_decimal_hash

SEED_LENGTH = 8
DEFAULT_STEP_DIVIDER = 3
STEP_DIVIDER_LENGTH = 1
MULTIPLIER_INTEGER = 1
DEFAULT_MULTIPLIER = math.pi


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class LinearCongruentGenerator:
    def __init__(self, seed_value=None, seed_length: int = SEED_LENGTH,
                 step_divider: int = DEFAULT_STEP_DIVIDER, multiplier: float = None):
        self._seed = get_decimal_hash(id(self), seed_length) \
            if seed_value is None else get_decimal_hash(seed_value, seed_length)

        _seed_hash = get_decimal_hash(self._seed, seed_length)

        self._step_divider = step_divider \
            if get_decimal_hash(self._seed, STEP_DIVIDER_LENGTH) == 0 \
            else get_decimal_hash(self._seed, STEP_DIVIDER_LENGTH)

        self._multiplier = MULTIPLIER_INTEGER + (_seed_hash / (10 ** get_digits_count(_seed_hash))) \
            if multiplier is None else multiplier

        self._sequence = iter(self._lcg(self._seed))

    def _lcg(self, max):
        current = self._seed
        step = max // self._step_divider
        while True:
            next = (current * self._multiplier + step) % max
            yield next
            current = next

    def seed(self, value, seed_length=SEED_LENGTH):
        """Change object instance seed parameters"""
        pass

    def get_current_status(self):
        print(self._seed, self._step_divider, self._multiplier)

    def randint(self, min: int, max: int):
        result = round(next(self._sequence)) % (max + 1)
        if result < min:
            return result + min
        else:
            return result

    def randfloat(self, min: float, max: float):
        result = next(self._sequence) % max
        if result < min:
            return result + min
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
