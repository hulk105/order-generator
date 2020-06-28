import unittest
from generators import *
from myconfigparser import config
from constants import *
import itertools as it

# DICT KEYS
first_entry = 'first_entry'
step = 'step'
multiplier = 'multiplier'
max_entry = 'max_entry'
values = 'values'


for i in it.chain(range(30, 52), range(1, 18)):
    print(i)


class OrderIdGeneratorTest(unittest.TestCase):
    def test(self):
        pass


class ProviderIdGeneratorTest(unittest.TestCase):
    def test(self):
        pass


class DirectionGeneratorTest(unittest.TestCase):
    def test(self):
        pass
