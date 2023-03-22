def pascal(n):

    l = [[1], [1, 1]]

    for i in range(2, n + 1):
        k = list()
        k.append(1)
        for j in range(0, len(l[i-1]) - 1):
            k.append(l[i - 1][j] + l[i - 1][j + 1])
        k.append(1)
        l.append(k)

    return l[n]


n = int(input())
for i in range(n):
    print(*pascal(i))

