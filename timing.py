"""
Author: Alan Lai

Task:
    Use context manager for timing code

>>> from time import sleep
>>> with timing():
...    sleep(10)
Time spend 10.00s
"""
import time
from contextlib import contextmanager


@contextmanager
def timing():
    before = time.time()
    yield
    after = time.time()
    print("Time spend {:.2f}s".format(after - before))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
