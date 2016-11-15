"""
Author: Alan Lai

Task:
Implements count sort, assumeing element is less than 10.

>>> count_sort([4, 1, 3, 4, 3])
[1, 3, 3, 4, 4]
"""


def count_sort(L):
    k = 10  # assume element belongs to [0, 9)
    C = [0] * k
    for i in L:
        C[i] += 1
    C_cum = [0] * k
    for i in range(k):
        if i == 0:
            C_cum[i] = C[i]
        else:
            C_cum[i] = C_cum[i - 1] + C[i]
    res = [None] * len(L)
    for j in reversed(L):
        res[C_cum[j] - 1] = j
        C_cum[j] -= 1
    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod()
