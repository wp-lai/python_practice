"""
Author: Alan Lai

Task:
Implementing heapsort alogrithm

>>> heapsort([3, 2, 1, 4])
[1, 2, 3, 4]
>>> heapsort([5, 39, 434, 22, 43, 857, 4, 58])
[4, 5, 22, 39, 43, 58, 434, 857]
"""
def heapsort(nums):
    # turn into max-heap
    n = len(nums)
    for i in range(n // 2)[::-1]:
        heapify(nums, i)

    # heapsort
    while n > 0:
        nums[0], nums[n-1] = nums[n-1], nums[0]
        n -= 1
        heapify(nums, 0, n)

    return nums


def heapify(nums, pos, len_limit=None):
    """
    >>> heapify([3, 2, 1, 4], 1)
    [3, 4, 1, 2]
    >>> heapify([3, 4, 1, 2], 0)
    [4, 3, 1, 2]
    >>> heapify([2, 3, 1], 0)
    [3, 2, 1]
    >>> heapify([1, 2], 0)
    [2, 1]
    """
    n = len(nums)
    if len_limit is None:
        len_limit = n
    while pos < len_limit // 2:
        left_child = pos * 2 + 1
        right_child = (pos + 1) * 2
        if right_child < len_limit:
            max_val = max(nums[pos], nums[left_child], nums[right_child])
        else:
            max_val = max(nums[pos], nums[left_child])
        if max_val == nums[pos]:
            break
        elif max_val == nums[left_child]:
            nums[pos], nums[left_child] = nums[left_child], nums[pos]
            pos = left_child
        elif max_val == nums[right_child]:
            nums[pos], nums[right_child] = nums[right_child], nums[pos]
            pos = right_child
    return nums


if __name__ == '__main__':
    import doctest
    doctest.testmod()
