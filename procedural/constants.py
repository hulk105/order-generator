import os
from pathlib import Path


APP_NAME = 'order_history_generator'
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


# Log
LOG_FILENAME = str(APP_NAME + '.log')
LOG_DEFAULT_FORMAT = '%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s'


# CONFIG
CONFIG_FILENAME = 'config.yaml'
CONFIG_PATH = Path(PROJECT_DIR) / CONFIG_FILENAME
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S.%f'


# SQL
TABLE_NAME = 'Orders'
SQL_DUMP_FILENAME = 'orders_history_dump.sql'


# GENERATOR
