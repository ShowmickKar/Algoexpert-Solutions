# Problem Link: https://www.algoexpert.io/questions/Find%20Three%20Largest%20Numbers
# Time Complexity: O(N)
# Space Complexity: O(1)

import math


def findThreeLargestNumbers(array):
    indices = [-1 for _ in range(3)]
    nums = [-math.inf for _ in range(3)]
    for x in range(len(indices) - 1, -1, -1):
        for i in range(len(array)):
            if i == indices[1] or i == indices[-1]:
                continue
            if array[i] > nums[x]:
                nums[x] = array[i]
                indices[x] = i
    return nums
