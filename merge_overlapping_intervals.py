# Problem Link: https://www.algoexpert.io/questions/Merge%20Overlapping%20Intervals
# Time Complexity: O(nlogn)
# Space Complexity: O(n)

def mergeOverlappingIntervals(intervals):

    if not len(intervals):
        return []

    intervals.sort()

    result = [intervals[0]]

    for i in range(1, len(intervals)):
        if intervals[i][0] <= result[-1][-1]:
            if intervals[i][1] > result[-1][-1]:
                result[-1][-1] = intervals[i][1]
        else:
            result.append(intervals[i])

    return result
