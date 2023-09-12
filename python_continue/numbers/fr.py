from fractions import Fraction
from math import *
# s = '0.78 4.mini_projects 9.6 mini_projects.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 mini_projects.24 8.57 0.10 8.57 1.49 5.64 mini_projects.63 8.36 1.56 6.67 1.46' \
#     ' 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03' \
#     ' 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'
#
# l = s.split()
#
# print(Fraction(max(l)) + Fraction(min(l)))
#

# n = int(input())
# total = 0
# for i in range(1, n + 1):
#     total += Fraction(1, factorial(i))
# print(Fraction(total))

out = []
n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        num = Fraction(i, j)
        if num < 1 and gcd(i, j) == 1:
            out.append(num)
print(*sorted(out), sep='\n')
