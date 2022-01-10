# Problem Link: https://www.algoexpert.io/questions/Generate%20Document

def generateDocument(characters, document):
    frequencies = {}
    for ch in characters:
        frequencies[ch] = frequencies.get(ch, 0) + 1
    for ch in document:
        if ch in frequencies and frequencies[ch]:
            frequencies[ch] -= 1
        else:
            return False
    return True
