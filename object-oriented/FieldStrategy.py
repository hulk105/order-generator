import logging
import string
import sys
from abc import ABC, abstractmethod

from Exceptions import *
from LCGenerator.Random import random

BASE = 16
ORDER_ID_HEX_DEFAULT_STRING = 'deadbeef'
ORDER_ID_RAND_RANGE = 10, 20


class FieldStrategy(ABC):
    @abstractmethod
    def next_entry(self):
        pass


class IncrementalFieldStrategy(FieldStrategy):
    def next_entry(self):
        pass


class RandomFieldStrategy(FieldStrategy):
    def next_entry(self):
        pass


class OrderIDFieldStrategy(IncrementalFieldStrategy):
    def __init__(self, initial_order_id_hex_string: str):
        try:
            if all(character in string.hexdigits for character in initial_order_id_hex_string) is True:
                self.order_id = int(initial_order_id_hex_string, BASE)
            else:
                raise HexStringError(initial_order_id_hex_string)
        except HexStringError as e:
            logging.error(f"{e}. Set to default string '{ORDER_ID_HEX_DEFAULT_STRING}'")
            self.order_id = int(ORDER_ID_HEX_DEFAULT_STRING, BASE)

    def next_entry(self):
        self.order_id += random.randint(*ORDER_ID_RAND_RANGE)
        return hex(self.order_id)


class Context:
    def __init__(self, strategy: FieldStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: FieldStrategy) -> None:
        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        return self._strategy.next_entry()


context = Context(OrderIDFieldStrategy('deadbeefg'))
for i in range(10):
    print(context.do_some_business_logic())
