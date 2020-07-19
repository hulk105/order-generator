import logging

from pypika import Table, Query

import constants as const
from utils import benchmark_function


@benchmark_function
def write_sql_dump(*args):
    orders_table = Table(const.TABLE_NAME)
    sql_dump_file = open(const.SQL_DUMP_FILENAME, 'w')
    logging.info('Writing SQL dump to %s as %s' % (sql_dump_file.name, sql_dump_file.encoding))
    # Generate DB query
    query = Query.into(orders_table).insert(*args)
    sql_dump_file.write(str(query) + '\n')
