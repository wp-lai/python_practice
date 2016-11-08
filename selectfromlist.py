"""
Author: Alan Lai

Question:
Given a list of data, and a list of boolean value as selector,
Form a list of selected data, choose element from data whenever
the cooresponding item in selector is truthy.

>>> data = [2, 3, 4, 5]
>>> selector = [True, True, False, True]
>>> select_from_list(data, selector)
[2, 3, 5]
"""


# Solution 1: using generator comprehension
def select_from_list(data, selector):
    return (e for e, s in zip(data, selector) if s)


# Solution 2: using itertools.compress
def select_from_list(data, selector):
    from itertools import compress
    return list(compress(data, selector))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
