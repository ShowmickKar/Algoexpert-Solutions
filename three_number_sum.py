# Problem Link: https://www.algoexpert.io/questions/Three%20Number%20Sum
# Time Complexity: O(N^2)
# Space Complexity: O(1)


def threeNumberSum(array, target):
    sum_of_pairs = {}  # int : list(tuples)

    already_taken_pairs = {}  # string : boolean

    result = []

    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] in sum_of_pairs:
                sum_of_pairs[array[i] + array[j]].append((i, j))
            else:
                sum_of_pairs[array[i] + array[j]] = [(i, j)]

    for i in range(len(array)):
        if target - array[i] in sum_of_pairs:
            for pair in sum_of_pairs[target - array[i]]:
                if pair[0] == i or pair[1] == i:
                    continue
                possible_triplet = sorted(
                    [array[i], array[pair[0]], array[pair[1]]])
                if str(possible_triplet) in already_taken_pairs:
                    continue
                result.append(possible_triplet)
                already_taken_pairs[str(possible_triplet)] = True

    result.sort()

    return result
