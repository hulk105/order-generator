import configparser

config = configparser.ConfigParser()

first_entry = 'first_entry'
step = 'step'
multiplier = 'multiplier'
max_entries = 'max_entries'

# CONSTANTS
config['CONSTANTS'] = {
    'ORDER_ID_INDEX': '1',
    'PROVIDER_ID_INDEX': '2',
    'DIRECTION_INDEX': '3',
    'CURRENCY_PAIR_INDEX': '4',
    'PX_INIT_INDEX': '5',
    'VOL_INIT_INDEX': '6',
    'PX_DELTA_INDEX': '7',
    'VOL_DELTA_INDEX': '8',
    'CREATION_DATE_INDEX': '9',
    'CHANGE_DATE_INDEX': '10',
    'STATUS_INDEX': '11',
}

ITERATIONS = 2000

# LCG PARAMS
ORDER_ID = {
    first_entry: 254781069873,
    step: 1354,
    multiplier: 1,
    max_entries: 549755813887,
}

PROVIDER_ID = {
    first_entry: 0,
    step: 0.33,
    multiplier: 1.333,
    max_entries: 1
}
PROVIDER_ID_VALUES = ['SQM', 'FXCM']

DIRECTION = {
    first_entry: 0,
    step: 0.76473,
    multiplier: 1.333,
    max_entries: 1
}
DIRECTION_VALUES = ['Buy', 'Sell']

CURRENCY_PAIR = {
    first_entry: 0,
    step: 1.3,
    multiplier: 3.5,
    max_entries: 19
}
CURRENCY_PAIR_DELTA = {
    first_entry: [256, 3],
    step: [1.333, 1.3],
    multiplier: [333, 4.77],
    max_entries: [1000, 100]
}
CURRENCY_PAIR_VALUES = [
    (['EUR', 'USD'], 1.120199),
    (['GBP', 'USD'], 1.304649),
    (['USD', 'CHF'], 0.984286),
    (['USD', 'JPY'], 112.175823),
    (['AUD', 'USD'], 0.677025),
    (['NZD', 'USD'], 0.648999),
    (['CAD', 'CHF'], 0.744244),
    (['CAD', 'JPY'], 84.706831),
    (['CHF', 'JPY'], 114.252908),
    (['EUR', 'AUD'], 1.712235),
    (['EUR', 'CAD'], 1.502292),
    (['EUR', 'CHF'], 1.072143),
    (['EUR', 'GBP'], 0.874086),
    (['EUR', 'JPY'], 121.346875),
    (['EUR', 'NZD'], 1.787336),
    (['GBP', 'AUD'], 1.981400),
    (['GBP', 'CAD'], 1.732194),
    (['NZD', 'CAD'], 0.861681),
    (['NZD', 'CHF'], 0.631029),
    (['NZD', 'JPY'], 71.310905),
]

with open('config.ini', 'w') as configfile:
    config.write(configfile)
