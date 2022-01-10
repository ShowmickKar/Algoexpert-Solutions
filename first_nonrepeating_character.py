# Problem Link: https://www.algoexpert.io/questions/First%20Non-Repeating%20Character

def firstNonRepeatingCharacter(string):
    frequency = {}
    for c in string:
        frequency[c] = frequency.get(c, 0) + 1
    for i in range(len(string)):
        if frequency[string[i]] == 1:
            return i
    return -1
