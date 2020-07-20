from typing import TextIO

from pypika import Table, Query


def write_sql_query(file: TextIO, table: str, *args):
    orders_table = Table(table)

    # Generate DB query
    query = Query.into(orders_table).insert(*args)
    file.write(str(query) + '\n')
