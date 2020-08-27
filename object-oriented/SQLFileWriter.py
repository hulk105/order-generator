from typing import TextIO

from pypika import Table, Query


class SQLFileWriter:
    def __init__(self, table, file: TextIO):
        self._table = Table(table)
        self.file = file

    def sql_insert(self, file: TextIO, columns, values):
        query = Query.into(self._table).columns(columns).insert(values)
        file.write(str(query) + ';\n')
