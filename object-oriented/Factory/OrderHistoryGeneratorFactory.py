from Factory.Interface import GeneratorFactory
from Factory import OrderHistoryGenerator


class OrderHistoryGeneratorFactory(GeneratorFactory):
    def create_generator(self, config):
        return OrderHistoryGenerator(config)
