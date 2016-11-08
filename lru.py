"""
Author: Alan Lai

Task:
Implementing Least Recently Used (LRU) cache
"""


def lru(func):
    known = {}

    def wrapper(arg):
        if arg not in known:
            known[arg] = func(arg)
        return known[arg]

    return wrapper


@lru
def fibonacci(n):
    """ Return fibonacci serias at position n

    >>> fibonacci(12)
    144
    >>> fibonacci(100)
    354224848179261915075
    """
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
