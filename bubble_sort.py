# Problem Link: https://www.algoexpert.io/questions/Bubble%20Sort
# Time Complexity: O(N^2)
# Space Complexity: O(1)

def bubbleSort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
