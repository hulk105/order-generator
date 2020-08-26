from abc import ABC, abstractmethod


class AbstractGenerator(ABC):
    @abstractmethod
    def generate_objects(self):
        pass
