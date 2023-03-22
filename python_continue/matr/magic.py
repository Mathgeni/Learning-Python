def magic(arr):
    flag = True
    comp = sum(arr[0])
    total3 = 0
    total4 = 0
    totals = list()
    for i in range(len(arr)):
        total1 = 0
        total2 = 0
        for j in range(len(arr)):
            totals.append(arr[i][j])
            total1 += arr[i][j]
            total2 += arr[j][i]
            if j + i == len(arr) - 1:
                total4 += arr[i][j]
        if total2 != comp or total1 != comp:
            flag = False
        total3 += arr[i][i]
    if total3 != comp or total4 != comp:
        flag = False
    totalc = [int(i) for i in range(1, len(arr) ** 2 + 1)]
    a = sorted(totalc)
    b = sorted(totals)
    if a != b or a[-1] == b[0]:
        flag = False
    return flag


n = int(input())
list1 = [input().split() for _ in range(n)]
for i in range(n):
    for j in range(n):
        list1[i][j] = int(list1[i][j])
if magic(list1):
    print('YES')
else:
    print('NO')
