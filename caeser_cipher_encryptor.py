# Problem Link: https://www.algoexpert.io/questions/Caesar%20Cipher%20Encryptor
# Time Complexity: O(N)
# Space Complexity: O(1)


import string


def caesarCipherEncryptor(input_string, key):
    alphabets = [letter for letter in string.ascii_lowercase]
    indices = {letter: i for i, letter in enumerate(alphabets)}

    res = ""
    key %= 26

    for c in input_string:
        cur_index = indices[c] + key
        if cur_index >= 26:
            cur_index -= 26
        res += alphabets[cur_index]
    return res
