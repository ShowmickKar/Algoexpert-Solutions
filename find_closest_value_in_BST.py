# problem Link: https://www.algoexpert.io/questions/Find%20Closest%20Value%20In%20BST

import math

def findClosestValueInBstHelper(tree, target, hash_value):
	if tree == None:
		return hash_value[1]
	if (abs(target - tree.value)) < abs(target - hash_value[1]):
		hash_value[1] = tree.value
	if target > tree.value:
		return findClosestValueInBstHelper(tree.right, target, hash_value)
	return findClosestValueInBstHelper(tree.left, target, hash_value)

def findClosestValueInBst(tree, target):
	hash_value = {1 : -math.inf}
	return findClosestValueInBstHelper(tree, target, hash_value)		

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
