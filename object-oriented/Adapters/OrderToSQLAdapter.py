from Factory import OrderHistoryGenerator
from SQLFileWriter import SQLFileWriter
from Constants import SQL_TABLE_COLUMNS


class OrderToSQLAdapter:
    def __init__(self, generator: OrderHistoryGenerator, writer: SQLFileWriter):
        self.order_history_generator = generator
        self.writer = writer
        self.new_orders_list = []

    def convert_orders(self):
        for order in self.order_history_generator.get_orders_list():
            for field in order[5:][0]:
                self.new_orders_list.append([*order[:5], *field])

    def write_orders_to_file(self):
        for order in self.new_orders_list:
            self.writer.sql_insert(file=self.writer.file, columns=SQL_TABLE_COLUMNS, values=order)
