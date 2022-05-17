# Problem Link: https://www.algoexpert.io/questions/Task%20Assignment

def taskAssignment(k, tasks):
    auxiliary_array = []
    for i in range(len(tasks)):
        auxiliary_array.append([tasks[i], i])
    auxiliary_array = sorted(auxiliary_array)
    l = 0
    r = len(tasks) - 1
    result = []
    while l < r:
        result.append([auxiliary_array[l][1], auxiliary_array[r][1]])
        l += 1
        r -= 1
    return result
