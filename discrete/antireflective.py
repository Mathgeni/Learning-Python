import random

x = 4
y = 4
array = [[random.randint(0, 1) for i in range(x)] for j in range(y)]
print(array)
print("ANTIREFLECTIVE:", end=' ')
m = [array[i][i] for i in range(x)]
if m[0] == 0 and m[1] == 0 and m[2] == 0 and m[3] == 0:
    print("YES")
else:
    print("NO")