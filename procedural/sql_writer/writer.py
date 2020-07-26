from typing import TextIO

from pypika import Table, Query


def sql_insert(file: TextIO, table: str, columns, values):
    orders_table = Table(table)

    # Generate DB query
    query = Query.into(orders_table).columns(columns).insert(values)
    file.write(str(query) + ';\n')
