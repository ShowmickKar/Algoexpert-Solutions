# Problem Link: https://www.algoexpert.io/questions/Array%20Of%20Products
# Time Complexity: O(N)
# Space Complexity: O(N)

def arrayOfProducts(array):
    from_left = array.copy()
    from_right = array.copy()
    result = []

    for i in range(1, len(array)):
        from_left[i] *= from_left[i - 1]

    for i in range(len(array) - 2, -1, -1):
        from_right[i] *= from_right[i + 1]

    for i in range(len(array)):
        if i == 0:
            result.append(from_right[i + 1])
        elif i == len(array) - 1:
            result.append(from_left[i - 1])
        else:
            result.append(from_left[i - 1] * from_right[i + 1])

    return result
