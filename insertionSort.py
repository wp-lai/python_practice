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
    numbers = numbers[:]  # if in-place sort, remove this line
    if len(numbers) <= 1:
        return numbers

    for i in range(1, len(numbers)):
        # swap to the insertion place
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = key

    return numbers


if __name__ == '__main__':
    import doctest
    doctest.testmod()
