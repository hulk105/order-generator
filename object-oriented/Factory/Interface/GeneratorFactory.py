from abc import ABC, abstractmethod


class GeneratorFactory(ABC):
    @abstractmethod
    def create_generator(self, config):
        pass
