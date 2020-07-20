def benchmark_function(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        return return_value, end - start

    return wrapper()


def get_digit(number, n) -> int:
    return number // 10 ** n % 10


def get_digits_count(number) -> int:
    from math import log10

    if number > 0:
        return int(log10(number)) + 1
    elif number == 0:
        return 1
    else:
        # +1 if you don't count the '-'
        return int(log10(-number)) + 2


def get_decimal_hash(value, length: int) -> int:
    from hashlib import sha1
    return int(sha1(str(value).encode('utf-8')).hexdigest(), 16) % (10 ** length)
