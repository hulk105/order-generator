from abc import ABC, abstractmethod


class FieldStrategy(ABC):
    @abstractmethod
    def get_current(self):
        pass

    @abstractmethod
    def next_entry(self, *args):
        pass
