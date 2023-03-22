def subs(arr):
    out = list()
    out.append([])
    for i in range(1, len(arr) + 1):
        for j in range(0, len(arr)):
            if len(arr[j:]) >= i:
                out.append(arr[j:j + i])
    return out


s = input().split()
print(subs(s))
