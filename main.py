'''
X - first entry
a - coeff
c - step
m - max entry
549755813887 = 7FFFFFFFFF
'''
import math


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

PHI = (math.sqrt(5) + 1) / 2

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

CURRENCY_PAIR = [
    (['EUR', 'USD'], 1.120199),
    (['GBP', 'USD'], 1.304649),
    (['USD', 'CHF'], 0.984286),
    (['USD', 'JPY'], 112.175823),
    (['AUD', 'USD'], 0.677025),
    (['NZD', 'USD'], 0.648999),
    (['CAD', 'CHF'], 0.744244),
    (['CAD', 'JPY'], 84.706831),
    (['CHF', 'JPY'], 114.252908),

EUR	AUD
EUR	CAD
EUR	CHF
EUR	GBP
EUR	JPY
EUR	NZD
GBP	AUD
GBP	CAD
NZD	CAD
NZD	CHF
NZD	JPY
]


def generate_order_id(iteration):
    return format(lcg(ORDER_ID.get(X), ORDER_ID.get(C), ORDER_ID.get(A), ORDER_ID.get(M), iteration), 'x')


def generate_provider_id(iteration):
    return PROVIDER_ID_VALUES[round(lcg(PROVIDER_ID.get(X), PROVIDER_ID.get(C), PROVIDER_ID.get(A), PROVIDER_ID.get(M),
                                        iteration))]


def generate_direction(iteration):
    return DIRECTION_VALUES[round(lcg(DIRECTION.get(X), DIRECTION.get(C), DIRECTION.get(A), DIRECTION.get(M),
                                      iteration))]


if __name__ == '__main__':
    for i in range(ITERATIONS):
        ORDERS[i].append(i)

        ORDERS[i].append(generate_order_id(i))
        ORDERS[i].append(generate_provider_id(i))
        ORDERS[i].append(generate_direction(i))


for order in ORDERS:
    print(order)
