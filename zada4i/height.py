def height(n, m):
    h, bk = 0, 1  # высота и нулевой биномиальный коэффициент
    for i in range(1, n + 1):
        print(bk)
        bk = bk * m // i
        h += bk
        m -= 1
    return h
