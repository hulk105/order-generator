from Strategies import *


class Context:
    def __init__(self, strategy: FieldGeneratingStrategy) -> None:
        self._strategy = strategy

    def get_strategy(self):
        return self._strategy

    def get_current(self):
        return self._strategy.get_current()

    def next_entry(self):
        return self._strategy.next_entry()


