import matplotlib.pyplot as plt
import math as m


def x(b, delta=0.0):
    def period(t):
        return m.sin(float(b) * float(t) + float(delta))
    return period


x1, x2 = float(-1.0), float(1.0)
scale = 1 * 10 ** (-5)

t = []
x1 = float(x1)
x2 = float(x2)
while x1 <= x2:
    t.append(x1)
    x1 += float(scale)
t.append(x2 + float(scale))

a = list(map(x(m.pi, delta=m.pi / 4), t))
y = list(map(x(m.pi), t))

fig, ax = plt.subplots()
ax.plot(a, y)
plt.show()
