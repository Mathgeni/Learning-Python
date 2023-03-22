s = input().split()
n = int(input())
out = list()
for i in range(0, len(s), n):
    out.append(s[i: i + n])

print(out)
