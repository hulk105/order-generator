import logging


def benchmark_function(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        logging.info('Finished in %s seconds' % str(end - start))
        return return_value

    return wrapper
