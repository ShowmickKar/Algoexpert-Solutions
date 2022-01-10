# Problem Link: https://www.algoexpert.io/questions/Class%20Photos


def classPhotos(redShirtHeights, blueShirtHeights):
    red = True
    blue = True
    redShirtHeights = sorted(redShirtHeights)
    blueShirtHeights = sorted(blueShirtHeights)

    for i in range(len(redShirtHeights)):
        if redShirtHeights[i] >= blueShirtHeights[i]:
            blue = False
        if redShirtHeights[i] <= blueShirtHeights[i]:
            red = False
        if not red and not blue:
            return False
    return red or blue
