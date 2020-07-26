import os
from pathlib import Path

APP_NAME = 'order_history_generator'
PROJECT_ABS_PATH = os.path.dirname(os.path.abspath(__file__))

# Log
LOG_FILENAME = str(APP_NAME + '.log')
LOG_DEFAULT_FORMAT = '%(asctime)s %(levelname)s %(message)s'
LOG_DEFAULT_LOGGING_LEVEL = 10
EXCEPTION_INFO = True

# RANDOM
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S.%f'
RANDOM_SEED = 'thisisrandomseeed'

# ORDER GENERATOR
ORDER_GENERATOR_DATA_PATH = 'order_history_generator/generator_data.yaml'
ORDER_GENERATOR_DATA_ABS_PATH = Path(PROJECT_ABS_PATH) / ORDER_GENERATOR_DATA_PATH

# SQL
TABLE_NAME = 'Orders'
SQL_DUMP_FILENAME = 'orders_history_dump.sql'
