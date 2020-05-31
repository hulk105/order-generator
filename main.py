"""
X - first entry
a - coeff
c - step
m - max entry
549755813887 = 7FFFFFFFFF
"""
import math


def lcg(x, c, a, m, iteration):
    count = 0
    temp = (a * x + c) % m
    while count != iteration:
        temp = (a * temp + c) % m
        count += 1
    return temp


# DICT KEYS
X = "X"
C = "c"
A = "a"
M = "m"
MAX_ENTRIES = "max_entries"

# CONSTANTS
ORDER_ID_INDEX = 1
PROVIDER_ID_INDEX = 2
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


def generate_order_id(x, c, a, m, iteration):
    return format(lcg(x, c, a, m, iteration), 'x')


def generate_provider_id(x, c, a, m, iteration):
    return PROVIDER_ID_VALUES[round(lcg(x, c, a, m, iteration))]


def generate_direction(x, c, a, m, iteration):
    return DIRECTION_VALUES[round(lcg(x, c, a, m, iteration))]


if __name__ == "__main__":
    for i in range(ITERATIONS):
        ORDERS[i].append(i)

        ORDERS[i].append(generate_order_id(ORDER_ID.get(X), ORDER_ID.get(C), ORDER_ID.get(A), ORDER_ID.get(M), i))
        ORDERS[i].append(generate_provider_id(PROVIDER_ID.get(X), PROVIDER_ID.get(C), PROVIDER_ID.get(A), PROVIDER_ID.get(M), i))
        ORDERS[i].append(generate_direction(DIRECTION.get(X), DIRECTION.get(C), DIRECTION.get(A), DIRECTION.get(M), i))


for order in ORDERS:
    print(order)
