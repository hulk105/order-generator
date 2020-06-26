import unittest
from generators import *
from myconfigparser import config

# DICT KEYS
first_entry = 'first_entry'
step = 'step'
multiplier = 'multiplier'
max_entry = 'max_entry'
values = 'values'


class OrderIdGeneratorTest(unittest.TestCase):
    def test(self):
        self.assertEqual(generate_order_id(
            config['ORDER_ID'][first_entry].get(int),
            config['ORDER_ID'][step].get(int),
            config['ORDER_ID'][multiplier].get(int),
            config['ORDER_ID'][max_entry].get(int),
            1,
        ), '3b52229f7b')


class ProviderIdGeneratorTest(unittest.TestCase):
    def test(self):
        self.assertEqual(generate_provider_id(
            config['PROVIDER_ID'][first_entry].get(int),
            config['PROVIDER_ID'][step].get(float),
            config['PROVIDER_ID'][multiplier].get(float),
            config['PROVIDER_ID'][max_entry].get(int),
            1,
            config['PROVIDER_ID'][values].get(),
        ), 'SQM')


class DirectionGeneratorTest(unittest.TestCase):
    def test(self):
        self.assertEqual(generate_provider_id(
            config['DIRECTION'][first_entry].get(int),
            config['DIRECTION'][step].get(float),
            config['DIRECTION'][multiplier].get(float),
            config['DIRECTION'][max_entry].get(int),
            1,
            config['DIRECTION'][values].get(),
        ), 'Sell')
