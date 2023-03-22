tele = {}
n = int(input())
for _ in range(n):
    number = input().lower().split()
    tele[number[1]] = tele.get(number[1], '') + number[0] + ' '

m = int(input())
for _ in range(m):
    name = input().lower()
    if name in tele:
        print(tele[name])
    else:
        print('абонент не найден')
