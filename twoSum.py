"""
Author: Alan Lai
Date: Oct 17, 2016

Question:
Given an array of integers, return indices of the two numbers 
such that they add up to a specific target.

>>> two_sum([3, 2, 4], 6)
[1, 2]

>>> two_sum([2, 7, 11, 15], 9)
[0, 1]

>>> two_sum([0, 2, 3, 0], 0)
[0, 3]
"""

# Solution 1: double loop
# Variation 1
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None


# Variation 2
def two_sum(nums, target):
    for i, left_num in enumerate(nums):
        for j, right_num in enumerate(nums[i+1:], start=i+1):
            if left_num + right_num == target:
                return [i, j]
    return None


# Variation 3
def two_sum(nums, target):
    found = [[i, j] 
             for i in range(len(nums)) 
             for j in range(i+1, len(nums))
             if nums[i] + nums[j] == target]
    if found:
        return found[0]
    else:
        return None


# Solution 2: two-pass hash table
def two_sum(nums, target):
    map_ = {}
    # build a {element: index} map 
    for i, num in enumerate(nums):
        map_[num] = i

    for j, num in enumerate(nums):
        complement = target - num
        if complement in map_ and \
           map_[complement] != j:
            return [j, map_[complement]]

    return None


# Solution 3: one-pass hash table
def two_sum(nums, target):
    map_ = {}
    
    # build map while iter
    for i, num in enumerate(nums):
        complement = target - num
        if complement in map_:
            return [map_[complement], i]
        map_[num] = i

    return None


if __name__ == '__main__':
    import doctest
    doctest.testmod()