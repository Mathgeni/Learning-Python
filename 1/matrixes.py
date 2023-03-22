import numpy as np

a = np.array([[0, 83, 0, 0, 0, 0, 0, 49],
              [0, 0, 13, 0, 71, 0, 0, 98],
              [0, 0, 0, 7, 0, 29, 31, 0],
              [0, 0, 0, 0, 0, 42, 0, 0],
              [0, 71, 0, 0, 0, 87, 0, 37],
              [0, 0, 29, 0, 87, 0, 0, 0],
              [0, 0, 31, 0, 57, 0, 0, 0],
              [49, 0, 0, 0, 37, 14, 0, 0]])
b = np.matmul(a, a)
c = np.matmul(b, b)
d = np.matmul(c, a)
# print(a)
# print()
# print(b)
# print()
# print(np.matmul(a, b))
# print()
# print(np.matmul(b, b))
print(d)