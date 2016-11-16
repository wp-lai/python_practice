"""
Task:
    Implement a Mirror class as a context manager
    within which the output text display in reversed order

References:
    "Fluent Python" Chapter 15

>>> with Mirror():
...    print("hello world!")
...
!dlrow olleh
>>> print("hello world!")
hello world!
"""


class Mirror(object):
    def __enter__(self):
        import sys
        self.writer = sys.stdout.write
        sys.stdout.write = self.reverse_writer

    def reverse_writer(self, text):
        return self.writer(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        import sys
        sys.stdout.write = self.writer


if __name__ == '__main__':
    import doctest
    doctest.testmod()
