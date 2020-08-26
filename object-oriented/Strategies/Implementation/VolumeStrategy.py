from Strategies.Interface import FieldStrategy
from LCGenerator import random
from Constants import DEFAULT_VOL_RANGE, DEFAULT_VOL_ROUND


class VolumeStrategy(FieldStrategy):
    def __init__(self):
        self._volume = self._random()

    def _random(self):
        return round(random.randfloat(*DEFAULT_VOL_RANGE), DEFAULT_VOL_ROUND)

    def get_current(self):
        return self._volume

    def volume(self, value):
        self._volume = value

    def next_entry(self, *args):
        self._volume = self._random()
        return self.get_current()
