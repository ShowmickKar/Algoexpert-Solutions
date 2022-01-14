# Problem Link: https://www.algoexpert.io/questions/First%20Duplicate%20Value
# Time Complexity: O(N)
# Space Complexity: O(1)


def firstDuplicateValue(array):
    for i in range(len(array)):
        if array[abs(array[i]) - 1] < 0:
            return abs(array[i])
        array[abs(array[i]) - 1] *= -1

    return -1
