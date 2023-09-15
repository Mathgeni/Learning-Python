def road():
    n, m = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(n)]
    max_road = [[[0, []] for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            best = max(max_road[i - 1][j][0], max_road[i][j - 1][0])
            if best == max_road[i - 1][j][0]:
                max_road[i][j][0] = table[i - 1][j - 1] + best
                max_road[i][j][1] = max_road[i - 1][j][1] + ['D']
            else:
                max_road[i][j][0] = table[i - 1][j - 1] + best
                max_road[i][j][1] = max_road[i][j - 1][1] + ['R']
    return max_road[-1][-1][0], max_road[-1][-1][1][1:]


if __name__ == '__main__':
    a, b = road()
    print(a)
    for i in b:
        print(i, end=' ')

