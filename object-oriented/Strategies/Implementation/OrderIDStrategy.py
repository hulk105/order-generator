import string

from Constants.Constants import HEX_BASE, DEFAULT_ORDER_ID_INCREMENT_RAND_RANGE
from Exceptions import *
from LCGenerator import random
from Strategies.Interface import FieldStrategy


def is_hexadecimal(hex_string: str):
    if all(character in string.hexdigits for character in hex_string) is True:
        return True
    else:
        raise HexStringError(hex_string)


class OrderIDStrategy(FieldStrategy):
    def __init__(self, initial_hex_string: str):
        is_hexadecimal(initial_hex_string)
        self._hex_as_int = int(initial_hex_string, HEX_BASE)

    def _increment(self):
        self._hex_as_int += random.randint(*DEFAULT_ORDER_ID_INCREMENT_RAND_RANGE)

    def get_current(self):
        return hex(self._hex_as_int)

    def next_entry(self):
        self._increment()
        return self.get_current()
