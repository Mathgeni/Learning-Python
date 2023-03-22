desk = [['.' for _ in range(8)] for _ in range(8)]
coor = input()
n = int(ord(str(coor[0])) - 97)
m = 7 - int(coor[1]) + 1
for i in range(8):
    for j in range(8):
        if i == m or j == n:
            desk[i][j] = '*'
        elif i + j == m + n:
            desk[i][j] = '*'
        elif n + i == j + m:
            desk[i][j] = '*'
desk[m][n] = 'Q'
for row in desk:
    print(*row)