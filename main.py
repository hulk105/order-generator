"""
X - first entry
a - coeff
c - step
m - max entry
549755813887 = 7FFFFFFFFF
"""
import math


def lcg(x, c, a, m):
    return (a * x + c) % m

print(lcg(0,4.33,1.333,1))

# DICT KEYS
X = "X"
C = "c"
A = "a"
M = "m"
MAX_ENTRIES = "max_entries"

# CONSTANTS
ORDER_ID_INDEX = 1
PROVIDER_ID_INDEX = 2
ENTRIES = 2000
ORDERS = [[] for i in range(ENTRIES)]

# LCG PARAMS
ORDER_ID = {
    X: 254781069873,
    C: 1354,
    A: 1,
    M: 549755813887,
}
PROVIDER_ID = {
    X: 0,
    C: 4.33,
    A: 1.333,
    M: 1
}
PROVIDER_ID_VALUES = ['SQM', 'FXCM']


def generate_order_id(x, c, a, m):
    return format(lcg(x, c, a, m), 'x')


def generate_provider_id(x, c, a, m):
    return PROVIDER_ID_VALUES[math.ceil(lcg(x, c, a, m))]


if __name__ == "__main__":
    for i in range(ENTRIES):
        ORDERS[i].append(i)

        if i == 0:
            ORDERS[i].append(format(ORDER_ID.get(X), 'x'))
            ORDERS[i].append(PROVIDER_ID_VALUES[PROVIDER_ID.get(X)])
        else:
            ORDERS[i].append(generate_order_id(int(ORDERS[i-1][ORDER_ID_INDEX], 16), ORDER_ID.get(C), ORDER_ID.get(A), ORDER_ID.get(M)))
            ORDERS[i].append(generate_provider_id(ORDERS[i-1][PROVIDER_ID_INDEX], PROVIDER_ID.get(C), PROVIDER_ID.get(A), PROVIDER_ID.get(M)))


for order in ORDERS:
    print(order)
