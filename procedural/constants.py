import os
import logging
from pathlib import Path


APP_NAME = 'order_history_generator'
PROJECT_ABS_PATH = os.path.dirname(os.path.abspath(__file__))


# Log
LOG_FILENAME = str(APP_NAME + '.log')
LOG_DEFAULT_FORMAT = '%(asctime)s %(levelname)s %(message)s'
LOG_DEFAULT_LOGGING_LEVEL = logging.DEBUG


# CONFIG
CONFIG_PATH = 'lcg_generator/config.yaml'
CONFIG_ABS_PATH = Path(PROJECT_ABS_PATH) / CONFIG_PATH
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S.%f'


# GENERATOR
GENERATOR_DATA_PATH = 'order_history_generator/generator_data.yaml'
GENERATOR_DATA_ABS_PATH = Path(PROJECT_ABS_PATH) / GENERATOR_DATA_PATH


# SQL
TABLE_NAME = 'Orders'
SQL_DUMP_FILENAME = 'orders_history_dump.sql'
