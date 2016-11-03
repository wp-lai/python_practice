"""
Author: Alan Lai

Question:
Build a generator that generates fibonacci series

>>> fib = fibonacci()
>>> next(fib)
0
>>> for i in range(5):
...     print(next(fib))
1
1
2
3
5
"""
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    import doctest
    doctest.testmod()