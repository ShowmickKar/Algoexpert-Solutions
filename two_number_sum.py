# Problem Link: https://www.algoexpert.io/questions/Two%20Number%20Sum

def twoNumberSum(array, targetSum):
	hash_val = {}
	for item in array:
		if targetSum - item in hash_val:
			return [item, targetSum - item]
		hash_val[item] = True
	return []
