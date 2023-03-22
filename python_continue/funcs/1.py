def matr(col=1, row=None, value=0):
    if row == None:
        row = col
    out = [[value for _ in range(row)] for _ in range(col)]
    return out


print(matr())
print(matr(3))
print(matr(2, 5))
print(matr(3, 4, 9))
