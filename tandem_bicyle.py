# Problem Link: https://www.algoexpert.io/questions/Tandem%20Bicycle
# Time Complexity: O(NLogN)
# Space Complexity: O(1)

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds = sorted(redShirtSpeeds)
    blueShirtSpeeds = sorted(blueShirtSpeeds, reverse=fastest)

    total = 0

    for i in range(len(redShirtSpeeds)):
        total += max(redShirtSpeeds[i], blueShirtSpeeds[i])

    return total
