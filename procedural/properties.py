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
TOTAL_ORDERS = config_parser['TOTAL_ORDERS'].get()
ZONES = config_parser['ZONES'].get()
DATE_FORMAT = '%Y-%m-%d %H:%M:%S.%f'
INITIAL_ORDER_ID = int(config_parser['INITIAL_ORDER_ID'].get(str), 16)
PROVIDER_ID = config_parser['PROVIDER_ID'][values].get()
DIRECTION = config_parser['DIRECTION'][values].get()
CURRENCY_PAIR = config_parser['CURRENCY_PAIR'][values].get()
TAGS = config_parser['TAGS'][values].get()
