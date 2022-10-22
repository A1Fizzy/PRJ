
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
pc1 = Point(4, 0)
pc2 = Point(9, 3)
pc3 = Point(3, 9)
pc4 = Point(2, 2)
pc5 = Point(8, 8)

class Order:
    def __init__(self, number, cords):
        self.number = number
        self.cords = cords

    def __str__(self):
        return f'Заказ {self.number}, с координатами {self.cords}'

o1 = Order(1, p1)
o2 = Order(2, p2)
o3 = Order(3, p3)
o4 = Order(4, p4)
o5 = Order(5, p5)
print(o1, o2, o3, o4, o5, sep='\n')

class Courier:
    def __init__(self, name, cordsC, speed):
        self.name = name
        self.cordsC = cordsC
        self.speed = speed

    def __str__(self):
        return f'Курьер {self.name}с координатами {self.cordsC} имеет скорость {self.speed}'

c1 = Courier('Walt ', pc1, 10)
c2 = Courier('Flin ', pc2, 10)
c3 = Courier('Jessi ', pc3, 10)
c4 = Courier('Hank ', pc4, 10)
c5 = Courier('Brandon ', pc5, 10)

print('\n', c1, c2, c3, c4, c5, sep='\n')
