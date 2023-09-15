def r():
    n, m = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(n)]
    road = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1:
                road[i][j] = table[i - 1][j - 1] + road[i][j - 1]
            elif j == 1:
                road[i][j] = table[i - 1][j - 1] + road[i - 1][j]
            else:
                road[i][j] = table[i - 1][j - 1] + min(road[i - 1][j], road[i][j - 1])
    return road[-1][-1]

if __name__ == '__main__':
    print(r())
