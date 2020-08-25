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
DEFAULT_TIME_DELTA = 100, 999999


class FieldStrategy(ABC):
    @abstractmethod
    def next_entry(self, *args):
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


class HexSequenceStrategy(FieldStrategy):
    def __init__(self, initial_hex_string: str):
        self._order_id = hex_to_int(initial_hex_string)

    def _increment(self):
        self._order_id += random.randint(*DEFAULT_ORDER_ID_INCREMENT_RAND_RANGE)
        return hex(self._order_id)

    def next_entry(self):
        return self._increment()


class RandomChoiceStrategy(FieldStrategy):
    def __init__(self, population: list):
        self._current = None
        self._population = population

    def _choice(self):
        self._current = random.choice(self._population)
        return self._current

    def next_entry(self):
        return self._choice()


class CurrencyPairStrategy(FieldStrategy):
    def __init__(self, currency_pairs: dict):
        self._currency_pairs = list(currency_pairs.items())
        self._current = None

    def _choice(self):
        self._current = list(random.choice(self._currency_pairs))

    def apply_delta(self):
        self._current[1] = round(random.add_random_delta(*DEFAULT_CURRENCY_RANDOM_RANGE_DELTA, self._current[1]), 6)
        return self._current

    def next_entry(self):
        self._choice()
        return self.apply_delta()


class DateStrategy(FieldStrategy):
    def __init__(self, initial_date: str, end_date: str, steps: int):
        self._initial_date = datetime.strptime(initial_date, DEFAULT_DATE_FORMAT)
        self._end_date = datetime.strptime(end_date, DEFAULT_DATE_FORMAT)
        self._current = self._initial_date
        self._timedelta = (self._end_date - self._initial_date) / steps

    def increment(self):
        self._current += self._timedelta + timedelta(microseconds=random.randint(*DEFAULT_TIME_DELTA))
        return self._current

    def get_timedelta(self):
        return self._timedelta

    def next_entry(self):
        return self.increment()


class Context:
    def __init__(self, strategy: FieldStrategy) -> None:
        self._strategy = strategy

    def get_strategy(self):
        return self._strategy

    def next_entry(self) -> None:
        return self._strategy.next_entry()


order_id_context = Context(HexSequenceStrategy(generator_config.initial_order_id))
provider_id_context = Context(RandomChoiceStrategy(generator_config.provider_id))
direction_context = Context(RandomChoiceStrategy(generator_config.direction))
currency_pair_context = Context(CurrencyPairStrategy(generator_config.currency_pairs))
date_context = Context(DateStrategy(generator_config.zones['RED']['initial_date'],
                                    generator_config.zones['RED']['end_date'], 300))

for i in range(50):
    print(order_id_context.next_entry(),
          provider_id_context.next_entry(),
          direction_context.next_entry(),
          currency_pair_context.next_entry(),
          date_context.next_entry(),
          )
