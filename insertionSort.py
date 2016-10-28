"""
Author: Alan Lai

Task:
Implementing insertion sort

>>> insert_sort([3, 2, 5, 6, 8])
[2, 3, 5, 6, 8]
>>> insert_sort([1])
[1]
>>> insert_sort([])
[]
"""
def insert_sort(numbers):
    numbers = numbers[:]
    if len(numbers) <= 1:
        return numbers

    for i in range(1, len(numbers)):
        while i > 0 and numbers[i-1] > numbers[i]:
            numbers[i-1], numbers[i] = numbers[i], numbers[i-1]
            i -= 1

    return numbers


if __name__ == '__main__':
    import doctest
    doctest.testmod()
