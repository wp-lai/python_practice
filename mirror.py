"""
Task:
    Implement a Mirror context manager
    within which the output text display in reversed order

References:
    "Fluent Python" Chapter 15

>>> with Mirror() as m:
...    print("hello world!")
...    print(m is None)
...
!dlrow olleh
eurT
>>> print("hello world!")
hello world!
"""
from contextlib import contextmanager


@contextmanager
def Mirror():
    # __enter__
    import sys
    old_writer = sys.stdout.write

    def reverse_writer(text):
        return old_writer(text[::-1])

    sys.stdout.write = reverse_writer

    try:
        yield
    finally:
        # __exit__
        sys.stdout.write = old_writer


# Equals to the following
# class Mirror(object):
#     def __enter__(self):
#         import sys
#         self.writer = sys.stdout.write
#         sys.stdout.write = self.reverse_writer
#
#     def reverse_writer(self, text):
#         return self.writer(text[::-1])
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         import sys
#         sys.stdout.write = self.writer


if __name__ == '__main__':
    import doctest
    doctest.testmod()
