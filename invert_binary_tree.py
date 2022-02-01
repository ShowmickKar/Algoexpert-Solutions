# Problem Link: https://www.algoexpert.io/questions/Invert%20Binary%20Tree

def invertBinaryTree(tree):
    if tree == None:
        return
    tree.left, tree.right = tree.right, tree.left
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
