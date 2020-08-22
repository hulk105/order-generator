from abc import ABC, abstractmethod


class GeneratorFactory(ABC):
    @abstractmethod
    def create_generator(self):
        pass


class OrderHistoryGeneratorFactory(GeneratorFactory):
    def create_generator(self):
        return OrderHistoryGenerator()


class AbstractGenerator(ABC):
    @abstractmethod
    def generate_objects(self):
        pass


class OrderHistoryGenerator(AbstractGenerator):
    def generate_objects(self):
        return "Some objects"


order_history_generator = OrderHistoryGeneratorFactory().create_generator()
print(order_history_generator.generate_objects())


