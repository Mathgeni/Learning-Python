from math import *
desk = [['.' for _ in range(8)] for _ in range(8)]
coor = input()
n = int(ord(str(coor[0])) - 97)
m = int(coor[1]) - 1
desk[7 - m][n] = 'N'
for i in range(8):
    for j in range(8):
        if abs(j - n) == 1 and abs(i - 7 + m) == 2:
            desk[i][j] = '*'
        elif abs(j - n) == 2 and abs(i - 7 + m) == 1:
            desk[i][j] = '*'
for row in desk:
    print(*row)
