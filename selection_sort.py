# Problem Link: https://www.algoexpert.io/questions/Selection%20Sort
# Time Complexity: O(N^N)
# Space Complexity: O(1)

def selectionSort(array):
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        if j > i:
            array[i], array[min_index] = array[min_index], array[i]
    return array
