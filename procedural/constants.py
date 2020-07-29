import os
from pathlib import Path

APP_NAME = 'order_history_generator'
PROJECT_ABS_PATH = os.path.dirname(os.path.abspath(__file__))

# LOG
LOG_FILENAME = str(APP_NAME + '.log')
LOG_DEFAULT_FORMAT = '%(asctime)s %(levelname)s %(message)s'
LOG_DEFAULT_LOGGING_LEVEL = 10
EXCEPTION_INFO = True

# RANDOM
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S.%f'
RANDOM_SEED = 'thisisrandomseeed'

# ORDER GENERATOR
ORDER_GENERATOR_DATA_PATH = 'generator_data.yaml'
ORDER_GENERATOR_DATA_ABS_PATH = Path(PROJECT_ABS_PATH) / ORDER_GENERATOR_DATA_PATH

# YAML strings
TOTAL_ORDERS_KEY = 'TOTAL_ORDERS'
INITIAL_ORDER_ID_KEY = 'INITIAL_ORDER_ID'
PROVIDER_ID_KEY = 'PROVIDER_ID'
DIRECTION_KEY = 'DIRECTION'
CURRENCY_PAIR_KEY = 'CURRENCY_PAIR'
ZONES_KEY = 'ZONES'
ZONE_INITIAL_DATE_KEY = 'initial_date'
ZONE_END_DATE_KEY = 'end_date'
ZONE_PERCENT_OF_TOTAL_ORDERS_KEY = 'percent_of_total_orders'
ZONE_POSSIBLE_STATUSES_KEY = 'possible_statuses'
TAGS_KEY = 'TAGS'

# Statuses
NEW_KEY = 'New'
PARTIALLY_FILLED_KEY = 'Partially Filled'
REJECTED_KEY = 'Rejected'

# DB
DUMP_FILENAME = 'orders_history_dump.cql'
TABLE_NAME = 'orders.orders_history'
COLUMNS = (
    'order_id',
    'provider_id',
    'direction',
    'tags',
    'description',
    'extra_data',
    'creation_date',
    'change_date',
    'status',
    'currency',
    'px',
    'vol',
)
