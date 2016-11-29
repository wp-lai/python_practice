import random


def partition(nums, l=0, r=None):
    """
    >>> partition([6,4,2,3,9,8,9,4,7,6,1])
    6
    """
    if r is None:
        r = len(nums) - 1
    j = l
    x = nums[l]
    for i in range(l+1, r+1):
        if nums[i] <= x:
            j += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[l], nums[j] = nums[j], nums[l]
    return j


def quick_sort(nums, l=0, r=None):
    """
    >>> nums = [6,4,2,3,9,8,9,4,7,6,1]
    >>> quick_sort(nums)
    >>> nums
    [1, 2, 3, 4, 4, 6, 6, 7, 8, 9, 9]
    """
    if r is None:
        r = len(nums) - 1
    if l >= r:
        return
    k = random.randint(l, r)
    nums[k], nums[l] = nums[l], nums[k]
    j = partition(nums, l, r)
    quick_sort(nums, l, j-1)
    quick_sort(nums, j+1, r)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
