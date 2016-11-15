"""
Author: Alan Lai

Task:
Sorts integers from range [0, k)

>>> count_sort([4, 1, 3, 4, 3], 5)
[1, 3, 3, 4, 4]
"""


def count_sort(L, k):
    # build a counter
    C = [0] * k
    for i in L:
        C[i] += 1

    # build a cumulative counter
    C_cum = [0] * k
    for i in range(k):
        if i == 0:
            C_cum[i] = C[i]
        else:
            C_cum[i] = C_cum[i - 1] + C[i]

    # build output list
    output = [None] * len(L)
    for j in reversed(L):
        output[C_cum[j] - 1] = j
        C_cum[j] -= 1
    return output


if __name__ == '__main__':
    import doctest
    doctest.testmod()
