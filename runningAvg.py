"""
Author: Alan Lai

Question:
Compute running average of a list of data

>>> running_avg([5, 4, 2, 8, 7, 6])
[5.0, 4.5, 3.6666666666666665, 4.75, 5.2, 5.333333333333333]
"""
def running_avg(data):
    accumulate_sum = []
    running_sum = 0
    for i in data:
        running_sum += i
        accumulate_sum.append(running_sum)
    average = []
    for i, n in enumerate(accumulate_sum, start=1):
        average.append(n / float(i))
    return average


# wrap into one-liner
# itertools.accumulate only exists in  Python 3
from itertools import accumulate, starmap
def running_avg(data):
    return list(starmap(lambda i, n: n / i, enumerate(accumulate(data), 1)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

