# Problem Link: https://www.algoexpert.io/questions/Smallest%20Difference
# Time Complexity: O(nLogn)

import math


def smallestDifference(arr1, arr2):
    arr1.sort()
    arr2.sort()

    p1, p2 = 0, 0

    difference = math.inf
    indices = [-1, -1]

    while p1 < len(arr1) and p2 < len(arr2):
        cur_difference = abs(arr1[p1] - arr2[p2])
        if cur_difference == 0:
            return [arr1[p1], arr2[p2]]
        if cur_difference < difference:
            difference = cur_difference
            indices = [p1, p2]
        if arr1[p1] <= arr2[p2] and p1 + 1 < len(arr1):
            p1 += 1
        else:
            p2 += 1
    return [arr1[indices[0]], arr2[indices[1]]]
