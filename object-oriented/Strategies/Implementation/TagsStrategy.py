from LCGenerator import random
from Strategies import FieldGeneratingStrategy


class TagsGeneratingStrategy(FieldGeneratingStrategy):
    def __init__(self, population: list):
        self._population = population
        self._current = None
        self._choice()

    def _choice(self):
        self._current = random.choice(self._population)

    def get_current(self):
        return self._current

    def get_population(self):
        return self._population

    def next_entry(self):
        self._choice()
        return self.get_current()
