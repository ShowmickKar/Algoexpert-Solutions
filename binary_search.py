# Problem Link: https://www.algoexpert.io/questions/Binary%20Search
# Time Complexity: O(LogN)

def binarySearch(array, target, start=0, end=None):
    if end == None:
        end = len(array) - 1
    if start > end:
        return -1
    mid = (start + end)//2
    if array[mid] == target:
        return mid
    if target > array[mid]:
        return binarySearch(array, target, mid + 1, end)
    return binarySearch(array, target, start, mid - 1)
