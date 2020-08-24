import logging
import string
import sys
from abc import ABC, abstractmethod
from Config import OrderGeneratorConfig, YAMLConfig
from Exceptions import *
from LCGenerator.Random import random

generator_config = OrderGeneratorConfig(YAMLConfig('generator_data.yaml').get_config)

HEX_BASE = 16
DEFAULT_ORDER_ID_HEX_STRING = 'deadbeef'
DEFAULT_ORDER_ID_INCREMENT_RAND_RANGE = 10, 20
DEFAULT_CURRENCY_RANDOM_RANGE_DELTA = 0.000001, 0.00001


class FieldStrategy(ABC):
    @abstractmethod
    def next_entry(self):
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

    def next_entry(self):
        self._order_id += random.randint(*DEFAULT_ORDER_ID_INCREMENT_RAND_RANGE)
        return hex(self._order_id)


class RandomChoiceStrategy(FieldStrategy):
    def __init__(self, population: list):
        self._current = None
        self._population = population

    def next_entry(self):
        self._current = random.choice(self._population)
        return self._current


class Context:
    def __init__(self, strategy: FieldStrategy) -> None:
        self._strategy = strategy

    def next_entry(self) -> None:
        return self._strategy.next_entry()


order_id_context = Context(HexSequenceStrategy(generator_config.initial_order_id))
provider_id_context = Context(RandomChoiceStrategy(generator_config.provider_id))
direction_context = Context(RandomChoiceStrategy(generator_config.direction))
currency_pair_context = Context(RandomChoiceStrategy(generator_config.currency_pairs))
for i in range(50):
    print(order_id_context.next_entry(),
          provider_id_context.next_entry(),
          direction_context.next_entry(),
          currency_pair_context.next_entry(),
          )
