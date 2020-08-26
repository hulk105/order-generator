import logging
import sys
from Config import OrderGeneratorConfig, YAMLConfigProvider
from Factory import OrderHistoryGeneratorFactory


class Main:
    config = None

    def init(self):
        pass

    def setup(self):
        logging.basicConfig(level=logging.INFO)
        self.config = OrderGeneratorConfig(YAMLConfigProvider('generator_data.yaml').get_config)

    def workflow(self):
        order_history_generator = OrderHistoryGeneratorFactory().create_generator(config=self.config)
        order_history_generator.generate_objects()
        for order in order_history_generator.get_orders_list():
            print(order)

    def report(self):
        pass


if __name__ == '__main__':
    main = Main()
    try:
        main.init()
        main.setup()
        main.workflow()
        main.report()
    except Exception as e:
        logging.error(e, exc_info=True)
        sys.exit(1)
