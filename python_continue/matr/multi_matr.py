def mult(arr1, arr2):
    res = []
    n = len(arr1)
    m = len(arr2)
    k = len(arr2[0])
    for i in range(n):
        row = list()
        for j in range(k):
            total = 0
            for r in range(m):
                total += arr1[i][r] * arr2[r][j]
            row.append(total)
        res.append(row)
    return res


