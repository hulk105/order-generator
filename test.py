import unittest
import generators
from mylogging import logger
from myconfigparser import config


class OrderIdGeneratorTest(unittest.TestCase):
    def test(self):
        self.assertEqual(generators.generate_order_id(254781069873, 1354, 1, 549755813887, 1), '3b5222a4c5')


class ProviderIdGeneratorTest(unittest.TestCase):
    def test(self):
        self.assertEqual(generators.generate_provider_id(0, 0.33, 1.333, 1, 1, ['SQM', 'FXCM']), 'FXCM')


class DirectionGeneratorTest(unittest.TestCase):
    def test(self):
        self.assertEqual(generators.generate_direction(0, 0.76473, 1.333, 1, 1, ['Buy', 'Sell']), 'Sell')


print(config.get('PROVIDER_ID', 'values').split())
