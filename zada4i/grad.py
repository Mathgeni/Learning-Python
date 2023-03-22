import numpy as np
import matplotlib.pyplot as pl
import random as rd
import time

eps = 0.0001


def func(x):
    return 0.5 * x ** 2


def derivative(x):
    return func(x + eps) / eps - func(x) / eps


x_values = np.arange(-5.0, 5.0, 0.05)
y_values = np.array(list(map(func, x_values)))
start = rd.uniform(-5, -5)
print(start)

pl.ion()
fig, ax = pl.subplots()
ax.grid(True)
ax.plot(x_values, y_values)
point = ax.scatter(start, func(start), c='red')

while abs(derivative(start)) > eps:
    start -= 0.3 * derivative(start)
    point.set_offsets([start, func(start)])
    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.5)

print(start)

