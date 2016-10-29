"""
Author: Alan Lai

Task:
Using merge sort algorithm to sort an array of numbers

>>> merge_sort([2, 3, 1, 4])
[1, 2, 3, 4]
>>> merge_sort([1])
[1]
>>> merge_sort([])
[]
>>> merge_sort([4, 5, 8, 9, 3, 6])
[3, 4, 5, 6, 8, 9]
"""
def merge_sort(numbers):
    length = len(numbers)
    if length <= 1:
        return numbers
    left = merge_sort(numbers[:length // 2])
    right = merge_sort(numbers[length // 2:])
    return merge(left, right)


def merge(left, right):
    """merge two sorted array into a sorted array

    >>> merge([1, 3], [2, 4])
    [1, 2, 3, 4]
    >>> merge([2], [1])
    [1, 2]
    """
    i, j = 0, 0
    res = []

    while True:
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

        if i >= len(left):
            res.extend(right[j:])
            break
        if j >= len(right):
            res.extend(left[i:])
            break
    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod()