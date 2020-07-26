import logging
import sys

import yaml

import constants as const
from order_history_generator.generator import generate_orders_history
from sql_writer.writer import write_sql_query

"""Init"""
result_list = []

"""Setup"""
logging.basicConfig(level=const.LOG_DEFAULT_LOGGING_LEVEL,
                    filename=const.LOG_FILENAME, format=const.LOG_DEFAULT_FORMAT)
logger = logging.getLogger(const.APP_NAME)
logger.info('logger set up at %s, writing %s' % (logger.name, const.LOG_FILENAME))

data_file = open(const.ORDER_GENERATOR_DATA_ABS_PATH)
data = yaml.load(data_file, Loader=yaml.FullLoader)
sql_dump = open(const.SQL_DUMP_FILENAME, 'w')

if __name__ == '__main__':
    logger.info('%s started' % const.APP_NAME)
    logger.info('start generating orders')
    try:
        generate_orders_history(data, result_list)
    except Exception as e:
        logger.error(e, exc_info=const.EXCEPTION_INFO)
    else:
        logger.info('succsessfully generated %s zones' % len(result_list))

    if len(result_list) == 0:
        sys.exit(1)

    logger.info('writing sql dump to %s' % sql_dump.name)
    try:
        for i in result_list:
            for j in i:
                write_sql_query(sql_dump, const.TABLE_NAME, j)
    except Exception as e:
        logger.exception(e, exc_info=const.EXCEPTION_INFO)
    else:
        logger.info('succsessfully wrote to %s' % sql_dump.name)
logger.info('Done')
