# Problem Link: https://www.algoexpert.io/questions/Tournament%20Winner

def tournamentWinner(competitions, results):
    winners = {}
    cur_max_score = 0
    cur_winner = None
    for i in range(len(competitions)):
        results[i] = 0 if results[i] == 1 else 1
        cur = competitions[i][results[i]]
        if cur in winners:
            winners[cur] += 1
        else:
            winners[cur] = 1
        if winners[cur] > cur_max_score:
            cur_winner = cur
            cur_max_score = winners[cur]
    return cur_winner
