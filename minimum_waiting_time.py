# Problem Link: https://www.algoexpert.io/questions/Minimum%20Waiting%20Time

def minimumWaitingTime(queries):
    queries = sorted(queries)
	  res = 0
	  cur = 0
	  for i in range(len(queries) - 1):
		    cur += queries[i]
		    res += cur
	  return res
