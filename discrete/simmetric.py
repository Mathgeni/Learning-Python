import random


def transpose(matr):
    res = []
    n = len(matr)
    m = len(matr[0])
    for j in range(m):
        tmp = []
        for i in range(n):
            tmp = tmp + [matr[i][j]]
        res = res + [tmp]
    return res


x = 4
y = 4
array = [[random.randint(0, 1) for i in range(x)] for j in range(y)]
print(array)
print("SIMMETRIC")
a = transpose(array)
print(a)
if a == array:
    print("YES")
else:
    print("NO")
