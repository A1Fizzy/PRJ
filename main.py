import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def get_distance(self, other_point):
        x1 = self.x
        x2 = other_point.x
        y1 = self.y
        y2 = other_point.y
        dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return dist


f = open('points.txt', 'r')

d = f.read(4)
s = f.read(1)
d1 = f.seek(9)
s1 = f.read(1)
p1 = Point(int(s), int(s1))

d = f.seek(5)
s = f.read(1)
d1 = f.seek(9)
s1 = f.read(1)
p2 = Point(int(s), int(s1))

d = f.seek(2)
s = f.read(1)
d1 = f.seek(4)
s1 = f.read(1)
p3 = Point(int(s), int(s1))

d = f.seek(9)
s = f.read(1)
d1 = f.seek(3)
s1 = f.read(1)
p4 = Point(int(s), int(s1))

d = f.seek(1)
s = f.read(1)
d1 = f.seek(4)
s1 = f.read(1)
p5 = Point(int(s), int(s1))

d = f.seek(4)
s = f.read(1)
d1 = f.seek(0)
s1 = f.read(1)
pc1 = Point(int(s), int(s1))

d = f.seek(4)
s = f.read(1)
d1 = f.seek(9)
s1 = f.read(1)
pc2 = Point(int(s), int(s1))

d = f.seek(2)
s = f.read(1)
d1 = f.seek(8)
s1 = f.read(1)
pc3 = Point(int(s), int(s1))

d = f.seek(1)
s = f.read(1)
d1 = f.seek(1)
s1 = f.read(1)
pc4 = Point(int(s), int(s1))

d = f.seek(7)
s = f.read(1)
d1 = f.seek(7)
s1 = f.read(1)
pc5 = Point(int(s), int(s1))


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
print('\n')


class Courier:
    def __init__(self, name, cordsC, speed):
        self.name = name
        self.cordsC = cordsC
        self.speed = speed
        self.distance = 0

    def __str__(self):
        return f'{self.name}с координатами {self.cordsC} имеет скорость {self.speed}'


c1 = Courier('Курьер 1 ', pc1, 10)
c2 = Courier('Курьер 2 ', pc2, 10)
c3 = Courier('Курьер 3 ', pc3, 10)
c4 = Courier('Курьер 4 ', pc4, 10)
c5 = Courier('Курьер 5 ', pc5, 10)

print(c1, c2, c3, c4, c5, sep='\n')

plan = {'Курьер 1': [Order('A', p1), Order('B', p2)], 'Курьер 2': [Order('C', p3), Order('B', p4)]}


def get_full_path(plan, couriers):
    full_path = 0
    for courier in couriers:
        name = courier.name
        if name not in plan:
            continue
        for number, order in enumerate(plan[name]):
            full_path = + order.point.get_distance_to_center()

            if number == 0:
                full_path += courier.point.get_distance_to_other(order.point)
            else:
                full_path += order.point.get_distance_to_center()
    return full_path


couriers = []
couriers.append(c1)
couriers.append(c2)
couriers.append(c3)
couriers.append(c4)
couriers.append(c5)

orders = []
orders.append(o1)
orders.append(o2)
orders.append(o3)
orders.append(o4)
orders.append(o5)

print("\n")
for order_number in range(len(orders)):

    distances = []
    for courier_number in range(len(couriers)):
        distances.append(orders[order_number].cords.get_distance(couriers[courier_number].cordsC))
        couriers[courier_number].distance = orders[order_number].cords.get_distance(couriers[courier_number].cordsC)

    for courier_number in range(len(couriers)):
        if couriers[courier_number].distance == min(distances):
            print(f"Заказ {orders[order_number].number} доставит курьер {couriers[courier_number].name}")
