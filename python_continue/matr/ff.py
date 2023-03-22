def good(a):
    flag = True
    for i in 'anton':
        if i in a:
            a = a[a.find(i):]
        else:
            flag = False
            break
        num = 0

    return flag

counter = 1
l = list()
n = int(input())

for _ in range(n):
    s = input()
    if good(s):
        l.append(counter)
    counter += 1

print(*l)