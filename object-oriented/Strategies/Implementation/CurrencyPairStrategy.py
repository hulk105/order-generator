from Strategies import FieldGeneratingStrategy
from LCGenerator import random
from Constants import DEFAULT_CURRENCY_RANDOM_RANGE_DELTA, DEFAULT_ROUND


class CurrencyPairGeneratingStrategy(FieldGeneratingStrategy):
    def __init__(self, currency_pairs: dict):
        self._currency_pairs = list(currency_pairs.items())
        self._current_currency = None
        self._current_ratio = 0
        self._choice()

    def _choice(self):
        _current = list(random.choice(self._currency_pairs))
        self._current_currency = _current[0]
        self._current_ratio = _current[1]

    def delta(self):
        return round(random.add_random_delta(*DEFAULT_CURRENCY_RANDOM_RANGE_DELTA, self._current_ratio), DEFAULT_ROUND)

    def delta_current(self):
        self._current_ratio = self.delta()

    def get_current(self):
        return [self._current_currency, self._current_ratio]

    def next_entry(self):
        self._choice()
        self.delta_current()
        return self.get_current()
