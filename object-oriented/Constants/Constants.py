DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S.%f'
HEX_BASE = 16
DEFAULT_ORDER_ID_HEX_STRING = 'deadbeef01'
DEFAULT_ORDER_ID_INCREMENT_RAND_RANGE = 10, 20
DEFAULT_CURRENCY_RANDOM_RANGE_DELTA = 0.000001, 0.00001
DEFAULT_TIME_DELTA = 1, 3
DEFAULT_ROUND = 6
DEFAULT_VOL_RANGE = 100, 1000
DEFAULT_VOL_ROUND = 2

ZONE_INITIAL_DATE_KEY = 'initial_date'
ZONE_END_DATE_KEY = 'end_date'
ZONE_PERCENT_OF_TOTAL_ORDERS_KEY = 'percent_of_total_orders'
ZONE_POSSIBLE_STATUSES_KEY = 'possible_statuses'

CONFIG_FILE_PATH = 'generator_data.yaml'
SQL_FILE_PATH = 'dump.sql'
SQL_TABLE_NAME = 'Orders'
SQL_TABLE_COLUMNS = (
    'order_id',
    'provider_id',
    'direction',
    'tags',
    'creation_date',
    'status',
    'change_date',
    'currency',
    'vol',
)
