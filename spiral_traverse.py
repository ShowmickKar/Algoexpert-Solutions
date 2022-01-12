

def spiralTraverse(m):
    res = []

    r_s, r_e, c_s, c_e = 0, len(m), 0, len(m[0])

    while r_s < len(m) and c_s < len(m[0]) and r_e >= 0 and c_e >= 0:

        for i in range(c_s, c_e):
            res.append(m[r_s][i])
        r_s += 1

        for i in range(r_s, r_e):
            res.append(m[i][c_e])
        c_e -= 1

        for i in range(c_e - 1, c_s - 1, -1):
            res.append(m[r_e - 1][i])
        r_e -= 1

        for i in range(r_e - 1, r_s - 1, -1):
            res.append(m[i][c_s])
        c_s += 1

    return res
