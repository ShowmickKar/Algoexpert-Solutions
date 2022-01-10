# Problem Link: https://www.algoexpert.io/questions

def isPalindrome(string):
    n = len(string)

    m = n // 2 + n % 2

    for i in range(m):
        if string[i] != string[n - i - 1]:
            return False
    return True
