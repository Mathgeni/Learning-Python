import string
from random import *
import string as s
n, m = int(input()), int(input())
password = [i for i in s.digits + s.ascii_letters if i not in 'lI1oO0']
for _ in range(n):
    l, d, u = 0, 0, 0
    out = sample(password, m)
    while l < 2 and d < 2 and u < 2:
        for i in out:
            if i in s.ascii_lowercase:
                l += 1
            elif i in s.digits:
                d += 1
            else:
                u += 1
        if l == 0 or d == 0 or u == 0:
            out = sample(password, m)
            l, d, u = 0, 0, 0
    print(*out, sep='')
