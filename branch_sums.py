# Problem Link: https://www.algoexpert.io/questions/Branch%20Sums

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSumsHelper(root, cur_sum, ans):
	if root == None:
		return
	if root.left == None and root.right == None:
		ans.append(cur_sum + root.value)
		return		
	branchSumsHelper(root.left, cur_sum + root.value, ans)
	branchSumsHelper(root.right, cur_sum + root.value, ans)		
		
def branchSums(root):
	ans = []
    branchSumsHelper(root, 0, ans)
	return ans
