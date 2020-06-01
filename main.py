'''
X - first entry
a - coeff
c - step
m - max entry
549755813887 = 7FFFFFFFFF
'''
import math
import random


def lcg(x, c, a, m, iteration):
    count = 0
    temp = (a * x + c) % m
    while count != iteration:
        temp = (a * temp + c) % m
        count += 1
    return temp


# DICT KEYS
X = 'X'
C = 'c'
A = 'a'
M = 'm'
MAX_ENTRIES = 'max_entries'

# CONSTANTS
ORDER_ID_INDEX = 1
PROVIDER_ID_INDEX = 2
DIRECTION_INDEX = 3
CURRENCY_PAIR_INDEX = 4
PX_INIT_INDEX = 5
VOL_INIT_INDEX = 6
PX_DELTA_INDEX = 7
VOL_DELTA_INDEX = 8
CREATION_DATE_INDEX = 9
CHANGE_DATE_INDEX = 10
STATUS_INDEX = 11

ITERATIONS = 2000
ORDERS = [[] for i in range(ITERATIONS)]

# LCG PARAMS
ORDER_ID = {
    X: 254781069873,
    C: 1354,
    A: 1,
    M: 549755813887,
}

PROVIDER_ID = {
    X: 0,
    C: 0.33,
    A: 1.333,
    M: 1
}
PROVIDER_ID_VALUES = ['SQM', 'FXCM']

DIRECTION = {
    X: 0,
    C: 0.76473,
    A: 1.333,
    M: 1
}
DIRECTION_VALUES = ['Buy', 'Sell']

CURRENCY_PAIR = {
    X: 0,
    C: 1.3,
    A: 3.5,
    M: 19
}
CURRENCY_PAIR_DELTA = {
    X: [256, 3],
    C: [1.333, 1.3],
    A: [333, 4.77],
    M: [1000, 100]
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


def generate_order_id(iteration):
    return format(lcg(ORDER_ID.get(X), ORDER_ID.get(C), ORDER_ID.get(A), ORDER_ID.get(M), iteration), 'x')


def generate_provider_id(iteration):
    return PROVIDER_ID_VALUES[round(lcg(PROVIDER_ID.get(X), PROVIDER_ID.get(C), PROVIDER_ID.get(A), PROVIDER_ID.get(M),
                                        iteration))]


def generate_direction(iteration):
    return DIRECTION_VALUES[round(lcg(DIRECTION.get(X), DIRECTION.get(C), DIRECTION.get(A), DIRECTION.get(M),
                                      iteration))]


def generate_currency_pair(status, iteration):
    currency_pair = CURRENCY_PAIR_VALUES[round(lcg(
        CURRENCY_PAIR.get(X),
        CURRENCY_PAIR.get(C),
        CURRENCY_PAIR.get(A),
        CURRENCY_PAIR.get(M),
        iteration))]

    currency_pair_to_string = str(currency_pair[0][0] + '/' + currency_pair[0][1])
    delta = round(lcg(CURRENCY_PAIR_DELTA.get(X)[status], CURRENCY_PAIR_DELTA.get(C)[status],
                      CURRENCY_PAIR_DELTA.get(A)[status], CURRENCY_PAIR_DELTA.get(M)[status], iteration))

    delta_parity = round(lcg(CURRENCY_PAIR_DELTA.get(X)[status + 1], CURRENCY_PAIR_DELTA.get(C)[status + 1],
                             CURRENCY_PAIR_DELTA.get(A)[status + 1], CURRENCY_PAIR_DELTA.get(M)[status + 1], iteration))

    if delta_parity % 2 == 0:
        currency_pair_value = round(currency_pair[1] + delta * 0.00001, 6)
        return currency_pair_to_string, currency_pair_value
    else:
        currency_pair_value = round(currency_pair[1] - delta * 0.00001, 6)
        return currency_pair_to_string, currency_pair_value


if __name__ == '__main__':
    for i in range(ITERATIONS):
        ORDERS[i].append(i)

        ORDERS[i].append(generate_order_id(i))
        ORDERS[i].append(generate_provider_id(i))
        ORDERS[i].append(generate_direction(i))
        currency_pair = generate_currency_pair(0, i)
        ORDERS[i].append(currency_pair[0])
        ORDERS[i].append(currency_pair[1])

for order in ORDERS:
    print(order)
