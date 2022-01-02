# Problem Link: https://www.algoexpert.io/questions/Sorted%20Squared%20Array

def sortedSquaredArray(array):
  	positives = []
	negatives = []
	ans = []
	for item in array:
		if item < 0:
			negatives.append(-item)
		else:
			positives.append(item)
	p = 0
	n = len(negatives) - 1
	while p < len(positives) and n >= 0:
		if positives[p] < negatives[n]:
			ans.append(positives[p] ** 2)
			p += 1
		else:
			ans.append(negatives[n] ** 2)
			n -= 1
	while p < len(positives):
		ans.append(positives[p] ** 2)
		p += 1
	while n >= 0:
		ans.append(negatives[n] ** 2)
		n -= 1
	return ans
