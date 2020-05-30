"""
X - first entry
a - coeff
c - step
m - max entry
549755813887 = 7FFFFFFFFF
"""


def lcg(a, c, m, x):
    return (a * x + c) % m


# DICT KEYS
X = "X"
C = "c"
A = "a"
M = "m"
MAX_ENTRIES = "max_entries"

ENTRIES = 1

ORDERS = [[]*ENTRIES]

# CONSTANTS
ORDER_ID = {
    X: 254781069873,
    C: 1354,
    A: 1,
    M: 549755813887,
}

STATUS = 1


def generate_order_id(x, c, a, m):
    return lcg(a, c, m, x)


if __name__ == "__main__":
    for i in range(ENTRIES):
        for j in range(STATUS):
            ORDERS[i].append(generate_order_id(ORDER_ID.get(X), ORDER_ID.get(C), ORDER_ID.get(A), ORDER_ID.get(M)))

print(ORDERS)
