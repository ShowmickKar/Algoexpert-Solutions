# Problem link: https://www.algoexpert.io/questions/Binary%20Tree%20Diameter
# Difficulty: Medium
# Time Complexity: O(N) Space Complexity: O(N)

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def calculate_heights(node, heights):
    if node == None:
        heights[node] = 0
        return heights[node]
    h = max(calculate_heights(node.left, heights),
            calculate_heights(node.right, heights)) + 1
    heights[node] = h
    return heights[node]


def diameter(node, heights):
    if node == None:
        return 0
    return max(heights[node.left] + heights[node.right] + 1, diameter(node.left, heights), diameter(node.right, heights))


def binaryTreeDiameter(node):
    heights = {}
    calculate_heights(node, heights)
    return diameter(node, heights) - 1
