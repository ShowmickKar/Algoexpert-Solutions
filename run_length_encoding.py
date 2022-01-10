# Problem Link: https://www.algoexpert.io/questions/Run-Length%20Encoding
# Time Complexity: O(N)
# Space Complexity: O(1)

def runLengthEncoding(string):
    encoded_string = ""

    index = 0

    while index < len(string):
        i = index
        while i < len(string) and string[i] == string[index]:
            i += 1
        length = i - index
        while length > 9:
            length -= 9
            encoded_string += "9" + string[index]
        encoded_string += str(length) + string[index]
        index = i

    return encoded_string
