from mpmath import *
from math import *
mp.dps = 15; mp.pretty = True
tt = [0.001, 0.01, 0.1, 1, 10]
fp = lambda p: abs((0.02 * p + 100000) / (-102 * p**2 + 0.02 * p + 100000))
ft = lambda t: t*exp(-t)
print(ft(tt[0]),ft(tt[0])-invertlaplace(fp,tt[0],method='talbot'))
print(invertlaplace(fp,tt[0],method='talbot'))
