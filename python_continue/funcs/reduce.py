from operator import mul
from functools import reduce

result = reduce(mul, range(1, 6))
print(result)

