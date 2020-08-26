from Strategies import FieldGeneratingStrategy
from datetime import datetime, timedelta
from LCGenerator import random
from Constants import DEFAULT_TIME_DELTA, DEFAULT_DATE_FORMAT


class DateGeneratingStrategy(FieldGeneratingStrategy):
    def __init__(self, initial_date: str, end_date: str, steps: int):
        self._initial_date = datetime.strptime(initial_date, DEFAULT_DATE_FORMAT)
        self._end_date = datetime.strptime(end_date, DEFAULT_DATE_FORMAT)
        self._current = self._initial_date
        self._timedelta = (self._end_date - self._initial_date) / steps

    def delta(self):
        return self._timedelta + timedelta(seconds=random.randfloat(*DEFAULT_TIME_DELTA))

    def _increment(self):
        self._current += self.delta()

    def get_timedelta(self):
        return self._timedelta

    def get_current(self):
        return self._current

    def next_entry(self):
        self._increment()
        return self.get_current()
