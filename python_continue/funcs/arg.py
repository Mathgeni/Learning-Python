def mean(*args):
    total = 0
    j = 0
    for i in args:
        if type(i) is float or type(i) is int:
            i = float(i)
            total += i
            j += 1
    if total == 0 or j == 0:
        return 0.0
    return total / j


print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


