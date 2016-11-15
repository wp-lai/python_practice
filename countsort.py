"""
Author: Alan Lai

Task:
Sorts integers from range [0, k)

>>> count_sort([4, 1, 3, 4, 3], 5)
[1, 3, 3, 4, 4]
"""


def count_sort(L, k):
    # build a counter
    cnt = [0] * k
    for i in L:
        cnt[i] += 1

    # build a cumulative counter
    cum = [0] * k
    for i in range(k):
        if i == 0:
            cum[i] = cnt[i]
        else:
            cum[i] = cum[i - 1] + cnt[i]

    # build out list
    out = [None] * len(L)
    for j in reversed(L):
        out[cum[j] - 1] = j
        cum[j] -= 1
    return out


if __name__ == '__main__':
    import doctest
    doctest.testmod()
