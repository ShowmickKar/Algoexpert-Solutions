# Problem Link: https://www.algoexpert.io/questions/Non-Constructible%20Change

def nonConstructibleChange(coins):
	coins = sorted(coins)
	if not len(coins):
		return 1
    cur_sum = 0
	for i in range(len(coins)):
		if coins[i] > cur_sum + 1:
			return cur_sum + 1
		cur_sum += coins[i]	
    return cur_sum + 1
