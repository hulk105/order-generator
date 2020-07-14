from config_parser import config_parser

# Dictionary key strings
values = 'values'
statuses = 'statuses'
orders_count = 'orders_count'
initial_date = 'initial_date'
end_date = 'end_date'
delta = 'delta'


# Constants
SEED = config_parser['SEED'].get()
ZONES = config_parser['ZONES'].get()
DATE_FORMAT = '%Y-%m-%d %H:%M:%S.%f'
INITIAL_ORDER_ID = config_parser['INITIAL_ORDER_ID'].get(int)
PROVIDER_ID = config_parser['PROVIDER_ID'][values].get()
DIRECTION = config_parser['DIRECTION'][values].get()
CURRENCY_PAIR = config_parser['CURRENCY_PAIR'][values].get()
CURRENCY_PAIR_DELTA = config_parser['CURRENCY_PAIR'][delta].get(float)
TAGS = config_parser['TAGS'][values].get()
