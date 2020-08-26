from Strategies.Interface import FieldStrategy
from LCGenerator import random
from Constants import DEFAULT_VOL_RANGE, DEFAULT_VOL_ROUND


class VolumeStrategy(FieldStrategy):
    def __init__(self):
        self._volume = 0

    def get_current(self):
        return self._volume

    def volume(self, value):
        self._volume = value

    def next_entry(self, *args):
        self._volume = round(random.randfloat(*DEFAULT_VOL_RANGE), 2)
