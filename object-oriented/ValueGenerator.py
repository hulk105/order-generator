import logging
import string
import sys
from abc import ABC, abstractmethod
from Config import OrderGeneratorConfig, YAMLConfig
from Exceptions import *
from LCGenerator.Random import random
from datetime import datetime, timedelta

generator_config = OrderGeneratorConfig(YAMLConfig('generator_data.yaml').get_config)

DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S.%f'
HEX_BASE = 16
DEFAULT_ORDER_ID_HEX_STRING = 'deadbeef'
DEFAULT_ORDER_ID_INCREMENT_RAND_RANGE = 10, 20
DEFAULT_CURRENCY_RANDOM_RANGE_DELTA = 0.000001, 0.00001
DEFAULT_TIME_DELTA = 1, 3


class ValueGenerator(ABC):
    @abstractmethod
    def get_current(self):
        pass

    @abstractmethod
    def next_entry(self, *args):
        pass


class IncrementalStrategy(ValueGenerator):
    @abstractmethod
    def _increment(self):
        pass


class ChoiceStrategy(ValueGenerator):
    @abstractmethod
    def _choice(self):
        pass


class DeltaStrategy(ValueGenerator):
    @abstractmethod
    def delta(self):
        pass


def is_hexadecimal(hex_string: str):
    if all(character in string.hexdigits for character in hex_string) is True:
        return True
    else:
        raise HexStringError(hex_string)


def hex_to_int(hex_string: str):
    try:
        is_hexadecimal(hex_string)
        return int(hex_string, HEX_BASE)
    except HexStringError as e:
        raise InvalidConfigurationError(e)


class HexSequenceStrategy(IncrementalStrategy):
    def __init__(self, initial_hex_string: str):
        self._hex_as_int = hex_to_int(initial_hex_string)

    def _increment(self):
        self._hex_as_int += random.randint(*DEFAULT_ORDER_ID_INCREMENT_RAND_RANGE)

    def get_current(self):
        return hex(self._hex_as_int)

    def next_entry(self):
        self._increment()
        return self.get_current()


class RandomChoiceStrategy(ChoiceStrategy):
    def __init__(self, population: list):
        self._population = population
        self._current = None
        self._choice()

    def _choice(self):
        self._current = random.choice(self._population)

    def get_current(self):
        return self._current

    def get_population(self):
        return self._population

    def next_entry(self):
        self._choice()
        return self.get_current()


class CurrencyPairStrategy(ChoiceStrategy, DeltaStrategy):
    def __init__(self, currency_pairs: dict):
        self._currency_pairs = list(currency_pairs.items())
        self._current_currency = None
        self._current_ratio = 0
        self._choice()

    def _choice(self):
        _current = list(random.choice(self._currency_pairs))
        self._current_currency = _current[0]
        self._current_ratio = _current[1]

    def delta(self):
        return round(random.add_random_delta(*DEFAULT_CURRENCY_RANDOM_RANGE_DELTA, self._current_ratio), 6)

    def delta_current(self):
        self._current_ratio = self.delta()

    def get_current(self):
        return [self._current_currency, self._current_ratio]

    def next_entry(self):
        self._choice()
        self.delta_current()
        return self.get_current()


class DateStrategy(IncrementalStrategy, DeltaStrategy):
    def __init__(self, initial_date: str, end_date: str, steps: int):
        self._initial_date = datetime.strptime(initial_date, DEFAULT_DATE_FORMAT)
        self._end_date = datetime.strptime(end_date, DEFAULT_DATE_FORMAT)
        self._current = self._initial_date
        self._timedelta = (self._end_date - self._initial_date) / steps

    def delta(self):
        return self._timedelta + timedelta(seconds=random.randfloat(*DEFAULT_TIME_DELTA))

    def _increment(self):
        self._current += self.delta()

    def get_timedelta(self):
        return self._timedelta

    def get_current(self):
        return self._current

    def next_entry(self):
        self._increment()
        return self.get_current()


class Context:
    def __init__(self, strategy: (IncrementalStrategy, ChoiceStrategy, DeltaStrategy)) -> None:
        self._strategy = strategy

    def get_strategy(self):
        return self._strategy

    def get_current(self):
        return self._strategy.get_current()

    def next_entry(self):
        return self._strategy.next_entry()


order_id_context = Context(HexSequenceStrategy(generator_config.initial_order_id))
provider_id_context = Context(RandomChoiceStrategy(generator_config.provider_id))
direction_context = Context(RandomChoiceStrategy(generator_config.direction))
currency_pair_context = Context(CurrencyPairStrategy(generator_config.currency_pairs))
date_context = Context(
    DateStrategy(generator_config.zones['RED']['initial_date'], generator_config.zones['RED']['end_date'], 300)
)
status_context = Context(RandomChoiceStrategy(generator_config.zones['RED']['possible_statuses']))

for i in range(50):
    print(
        order_id_context.next_entry(),
        provider_id_context.next_entry(),
        direction_context.next_entry(),
        currency_pair_context.next_entry(),
        date_context.next_entry(),
    )
    status_context.next_entry()
    for status in status_context.get_current():
        print(
            status,
            currency_pair_context.get_strategy().delta(),
            date_context.get_current() + date_context.get_strategy().delta(),
        )