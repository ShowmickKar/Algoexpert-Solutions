# Problem Link: https://www.algoexpert.io/questions/Validate%20BST

import math

# This is an input class. Do not edit.


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree, limit=[-math.inf, math.inf]):
    if tree == None:
        return True
    if tree.value < limit[0] or tree.value >= limit[-1]:
        return False
    return validateBst(tree.left, [limit[0], tree.value]) and validateBst(tree.right, [tree.value, limit[-1]])
