def knight(a, b):
    table = [[0 for _ in range(b)] for _ in range(a)]
    table[0][0] = 1
    for i in range(1, a):
        for j in range(1, b):
            if j - 2 < 0:
                table[i][j] = table[i - 2][j - 1]
            else:
                table[i][j] = table[i - 2][j - 1] + table[i - 1][j - 2]
    return table


if __name__ == '__main__':
    for i in knight(8, 3):
        print(i)
