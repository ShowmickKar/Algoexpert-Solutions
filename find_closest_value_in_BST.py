# problem Link: https://www.algoexpert.io/questions/Find%20Closest%20Value%20In%20BST

import math

def findClosestValueInBstHelper(tree, target, closest):
	if tree == None:
		return closest
	if abs(tree.value - target) < abs(closest - target):
		closest = tree.value
	if target > tree.value:
		return findClosestValueInBstHelper(tree.right, target, closest)
	return findClosestValueInBstHelper(tree.left, target, closest)

def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, math.inf)

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
