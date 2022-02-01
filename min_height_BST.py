# Problem Link: https://www.algoexpert.io/questions/Min%20Height%20BST

import math


def minHeightBst(array):
    dummy_root = BST(-math.inf)
    construct(0, len(array) - 1, array, dummy_root)
    return dummy_root.right


def construct(l, u, array, root):
    if (l > u):
        return
    mid = (l + u) // 2
    root.insert(array[mid])
    construct(l, mid - 1, array, root)
    construct(mid + 1, u, array, root)


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
