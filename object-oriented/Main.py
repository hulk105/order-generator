import logging
import sys
from Config import OrderGeneratorConfig, YAMLConfigProvider
from Factory import OrderHistoryGeneratorFactory
from Adapters.OrderToSQLAdapter import OrderToSQLAdapter
from SQLFileWriter import SQLFileWriter
from Constants import *


class Main:
    config = None
    sql_writer = None

    def init(self):
        pass

    def setup(self):
        logging.basicConfig(level=logging.INFO)
        self.config = OrderGeneratorConfig(YAMLConfigProvider(CONFIG_FILE_PATH).get_config)
        self.sql_writer = SQLFileWriter(file=open(SQL_FILE_PATH, 'w'), table=SQL_TABLE_NAME)

    def workflow(self):
        order_history_generator = OrderHistoryGeneratorFactory().create_generator(config=self.config)
        order_history_generator.generate_objects()
        adapter = OrderToSQLAdapter(order_history_generator, self.sql_writer)
        adapter.convert_orders()
        adapter.write_orders_to_file()

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
