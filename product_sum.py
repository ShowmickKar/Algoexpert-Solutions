# Problem Link: https://www.algoexpert.io/questions/Product%20Sum
# Time Complexity: O(n)
# Space Complexity: O(d)

def productSum(array, index=0, depth=1):
    print(depth)
    if index == len(array):
        return 0
    if isinstance(array[index], list):
        return (depth + 1) * productSum(array[index], 0, depth + 1) + productSum(array, index + 1, depth)
    return (array[index] + productSum(array, index + 1, depth))
