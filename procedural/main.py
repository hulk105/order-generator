import logging

import yaml

import constants as const
from order_history_generator import generator

"""Init"""
result_list = []

"""Setup"""
# Logger
logging.basicConfig(level=const.LOG_DEFAULT_LOGGING_LEVEL, filename=const.LOG_FILENAME, format=const.LOG_DEFAULT_FORMAT)
# Config
file = open(const.GENERATOR_DATA_ABS_PATH)
data = yaml.load(file, Loader=yaml.FullLoader)


if __name__ == '__main__':
    logging.info(const.APP_NAME + 'started')
    try:
        generator.generate_orders_history(data, result_list)
    except Exception as e:
        logging.error(e)
    logging.info('Done')
