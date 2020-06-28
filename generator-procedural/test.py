import unittest
from generators import *
from myconfigparser import config
from constants import *

# DICT KEYS
first_entry = 'first_entry'
step = 'step'
multiplier = 'multiplier'
max_entry = 'max_entry'
values = 'values'

for i in range(300):
    print(generate_random_number(
        first_entry=config[CURRENCY_PAIR]['delta1'][FIRST_ENTRY].get(int),
        step=config[CURRENCY_PAIR]['delta1'][STEP].get(float),
        multiplier=config[CURRENCY_PAIR]['delta1'][MULTIPLIER].get(float),
        max_entry=config[CURRENCY_PAIR]['delta1'][MAX_ENTRY].get(float),
        iteration=i,
    ), generate_random_number(
        first_entry=config[CURRENCY_PAIR]['delta2'][FIRST_ENTRY].get(int),
        step=config[CURRENCY_PAIR]['delta2'][STEP].get(float),
        multiplier=config[CURRENCY_PAIR]['delta2'][MULTIPLIER].get(float),
        max_entry=config[CURRENCY_PAIR]['delta2'][MAX_ENTRY].get(float),
        iteration=i,
    ))


class OrderIdGeneratorTest(unittest.TestCase):
    def test(self):
        pass


class ProviderIdGeneratorTest(unittest.TestCase):
    def test(self):
        pass


class DirectionGeneratorTest(unittest.TestCase):
    def test(self):
        pass
