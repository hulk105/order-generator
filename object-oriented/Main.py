import logging

from Config import OrderGeneratorConfig, YAMLConfigProvider
from GeneratorFactory import OrderHistoryGeneratorFactory


def init():
    pass


def setup():
    pass


def workflow():
    logging.basicConfig(level=logging.INFO)
    generator_config = OrderGeneratorConfig(YAMLConfigProvider('generator_data.yaml').get_config)
    order_history_generator = OrderHistoryGeneratorFactory().create_generator(config=generator_config)
    order_history_generator.generate_objects()

    for order in order_history_generator.get_orders_list():
        print(order)


def report():
    pass


if __name__ == '__main__':
    try:
        init()
        setup()
        workflow()
        report()
    except Exception as e:
        logging.error(e, exc_info=True)
