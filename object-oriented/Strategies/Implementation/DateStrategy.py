from Strategies.Interface import FieldStrategy
from datetime import datetime, timedelta
from LCGenerator import random
from Constants import DEFAULT_TIME_DELTA, DEFAULT_DATE_FORMAT


class DateStrategy(FieldStrategy):
    def __init__(self, initial_date: str, end_date: str, steps: int):
        self._initial_date = datetime.strptime(initial_date, DEFAULT_DATE_FORMAT)
        self._end_date = datetime.strptime(end_date, DEFAULT_DATE_FORMAT)
        self._creation_date = self._initial_date
        self._change_date = self._initial_date
        self._timedelta = (self._end_date - self._initial_date) / int(steps)

    def _increment(self):
        return self._timedelta + timedelta(seconds=random.randfloat(*DEFAULT_TIME_DELTA))

    def increment_creation_date(self):
        self._creation_date += self._increment()

    def increment_change_date(self):
        self._change_date += self._increment()

    def get_timedelta(self):
        return self._timedelta

    def get_current(self):
        return self._change_date

    def next_entry(self):
        self.increment_creation_date()
        self._change_date = self._creation_date
        return self.get_current()
