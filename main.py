import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __str__(self):
        return f'({self.x}, {self.y})'

    """
    def get_distance(self, other_point):
        x1 = self.x
        x2 = other_point.x
        y1 = self.y
        y2 = other_point.y
        dist = math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)
        return dist

#dist = p1.get_distance(p2)
"""
p1 = Point(1, 2)
p2 = Point(10, 6)
p3 = Point(3, 5)
p4 = Point(0, 4)
p5 = Point(2, 5)

class Order:
    def __init__(self, number, coords):
        self.number = number
        self.coords = coords

    def __str__(self):
        return f'Заказ {self.number}, с координатами {self.coords}'

o1 = Order(1, p1)
o2 = Order(2, p2)
o3 = Order(3, p3)
o4 = Order(4, p4)
o5 = Order(5, p5)
print(o1, o2, o3, o4, o5, sep = '\n')




