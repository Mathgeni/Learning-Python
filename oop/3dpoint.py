from random import *


class Point3D(object):
    """Point in 2 demention"""

    points = list()

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def append(self):
        Point3D.points.append((self.x, self.y))

    def get(self):
        return self.x, self.y

    def change(self, x, y):
        self.x = x
        self.y = y


class Point(Point3D):
    pass


for i in range(2):
    a = Point(*[int(i) for i in input().split()])
    if i % 2 == 0:          # Changing coordinates if i is odd
        a.change(5, 3)
    Point.append(a)

print(Point.points)

