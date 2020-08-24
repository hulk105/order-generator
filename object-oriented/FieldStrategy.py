import logging
import string
import sys
from abc import ABC, abstractmethod
from Config import YAMLConfig
from Exceptions import *
from LCGenerator.Random import random

config = YAMLConfig()

HEX_BASE = 16
DEFAULT_ORDER_ID_HEX_STRING = 'deadbeef'
DEFAULT_ORDER_ID_RAND_RANGE = 10, 20
TOTAL_ORDERS = 2000


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


class OrderIDFieldStrategy(FieldStrategy):
    def __init__(self, initial_order_id_hex_string: str):
        self._order_id = hex_to_int(initial_order_id_hex_string)

    def next_entry(self):
        self._order_id += random.randint(*DEFAULT_ORDER_ID_RAND_RANGE)
        return hex(self._order_id)


class Context:
    def __init__(self, strategy: FieldStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: FieldStrategy) -> None:
        self._strategy = strategy

    def execute(self) -> None:
        return self._strategy.next_entry()


order_id_context = Context(OrderIDFieldStrategy('deadbeef01g'))
for i in range(10):
    print(order_id_context.execute())
