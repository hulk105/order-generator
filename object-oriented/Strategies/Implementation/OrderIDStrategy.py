import string

from Constants.Constants import HEX_BASE, DEFAULT_ORDER_ID_INCREMENT_RAND_RANGE
from Exceptions import HexStringError
from LCGenerator import random
from Strategies.Interface import FieldStrategy


def is_hexadecimal(hex_string: str):
    if all(character in string.hexdigits for character in hex_string) is True:
        return True
    else:
        raise HexStringError(hex_string)


def hex_to_int(hex_string: str):
    try:
        is_hexadecimal(hex_string)
        return int(hex_string, HEX_BASE)
    except HexStringError:
        pass


class OrderIDStrategy(FieldStrategy):
    def __init__(self, initial_hex_string: str):
        self._hex_as_int = hex_to_int(initial_hex_string)

    def _increment(self):
        self._hex_as_int += random.randint(*DEFAULT_ORDER_ID_INCREMENT_RAND_RANGE)

    def get_current(self):
        return hex(self._hex_as_int)

    def next_entry(self):
        self._increment()
        return self.get_current()
