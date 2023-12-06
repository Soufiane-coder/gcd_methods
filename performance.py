from time import time


def performance(fn):
    def wrapper(*args, **kawargs):
        t1 = time()
        result = fn(*args, **kawargs)
        t2 = time()
        print(f'Time taken: {t2 - t1} seconds')
        return result
    return wrapper
