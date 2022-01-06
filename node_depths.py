# Problem Link: https://www.algoexpert.io/questions/Node%20Depths

def nodeDepthsHelper(root, depth):
    if root == None:
        return 0
    return (
        depth
        + nodeDepthsHelper(root.left, depth + 1)
        + nodeDepthsHelper(root.right, depth + 1)
    )


def nodeDepths(root):
    return nodeDepthsHelper(root, 0)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
