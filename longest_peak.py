# Problem Link: https://www.algoexpert.io/questions/Longest%20Peak

"""
Solution 01
Time Complexity: O(N) Space Complexity: O(N)
"""

def longestPeak(array):
    increasing_ending_indices = {}
    decreasing_starting_indices = {}

    cur_length = 1

    result = 0

    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            cur_length += 1
        else:
            increasing_ending_indices[i - 1] = cur_length
            cur_length = 1
    increasing_ending_indices[len(array) - 1] = cur_length

    # print(increasing_ending_indices)

    cur_length = 1
    cur_starting_index = 0

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            cur_length += 1
        else:
            decreasing_starting_indices[cur_starting_index] = cur_length
            cur_length = 1
            cur_starting_index = i
    decreasing_starting_indices[cur_starting_index] = cur_length

    # print(decreasing_starting_indices)

    for index in decreasing_starting_indices:
        if index in increasing_ending_indices:
            if increasing_ending_indices[index] < 2 or decreasing_starting_indices[index] < 2:
                continue
            result = max(
                result, increasing_ending_indices[index] + decreasing_starting_indices[index] - 1)
    # print(result)
    return result

"""
Solution 02
Time Complexity: O(N) Space Complexity: O(1)
"""

def longestPeak(array):
    res = 0

    starting_index = 0

    ending_index = 0

    while starting_index < len(array) - 1:
        i = starting_index + 1
        while i < len(array) and array[i] > array[i - 1]:
            i += 1
        if i - starting_index < 2:
            starting_index += 1
            continue
        j = i
        while j < len(array) and array[j] < array[j - 1]:
            j += 1
        if j > i and i - 1 > starting_index:
            res = max(res, j - starting_index)
            j -= 1
        starting_index = j

    return res
