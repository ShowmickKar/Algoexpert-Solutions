# Problem Link: https://www.algoexpert.io/questions/Insertion%20Sort
# Time Compleity: O(N^2)

def insertionSort(array):
    for i in range(1, len(array)):
        cur = array[i]
        for j in range(i - 1, -1, -1):
            if cur >= array[j]:
                break
            array[j + 1] = array[j]
            array[j] = cur
    return array
