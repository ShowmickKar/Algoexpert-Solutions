# Problem Link: https://www.algoexpert.io/questions/Monotonic%20Array
# Time Complexity: O(n)
# Space Complexity: O(1)

def isMonotonic(array):
    increasing = False
    decreasing = False
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            decreasing = True
        if array[i] > array[i - 1]:
            increasing = True
    return not(increasing and decreasing)
