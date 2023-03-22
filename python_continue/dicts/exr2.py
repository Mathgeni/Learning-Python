n = int(input())
d = {}
for _ in range(n):
    a, b, c = input().split()
    if a not in d:
        d.setdefault(a, {b: 0})
    if b not in d[a]:
       d[a].update({b: int(c)})
    elif b in d[a]:
        d[a][b] = d[a].get(b) + int(c)
out = [[key, value] for key, value in d.items()]
out.sort()

for i in out:
    print(f'{i[0]}:')
    m = [[j, k] for j, k in i[1].items()]
    m.sort()
    for i in m:
        print(*i)
