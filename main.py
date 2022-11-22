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
    def __init__(self, number, cords, weight):
        self.number = number
        self.cords = cords
        self.weight = weight

    def __str__(self):
        return f'Заказ {self.number}, с координатами {self.cords} весит {self.weight} кг'


o1 = Order(1, p1, 2)
o2 = Order(2, p2, 3)
o3 = Order(3, p3, 1)
o4 = Order(4, p4, 6)
o5 = Order(5, p5, 9)
print(o1, o2, o3, o4, o5, sep='\n')
print('\n')


class Courier:
    def __init__(self, name, cordsC, speed, load):
        self.name = name
        self.cordsC = cordsC
        self.speed = speed
        self.load = load
        self.distance = 0

    def __str__(self):
        return f'{self.name}с координатами {self.cordsC} имеет скорость {self.speed * 1000} км/ч и грузоподъёмность {self.load} кг'


c1 = Courier('Курьер 1, пеший ', pc1, 0.006, 2)
c2 = Courier('Курьер 2, пеший ', pc2, 0.006, 2)
c3 = Courier('Курьер 3, на велосипеде ', pc3, 0.012, 4)
c4 = Courier('Курьер 4, на велосипеде ', pc4, 0.012, 4)
c5 = Courier('Курьер 5, на автомобиле ', pc5, 0.06, 50)

print(c1, c2, c3, c4, c5, sep='\n')

plan = {'Курьер 1': [Order('A', p1, 2), Order('B', p2, 3)], 'Курьер 2': [Order('C', p3, 1), Order('D', p4, 6)]}


def get_full_path(plan, couriers):
    full_path = 0
    for courier in couriers:
        name = courier.name
        if name not in plan:
            continue
        for number, order in enumerate(plan[name]):
            full_path += order.point.get_distance_to_center()

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

#for order_number in range(len(orders)):
distances = []
for courier_number in range(len(couriers)):
    distances.append(orders[0].cords.get_distance(couriers[courier_number].cordsC))
    couriers[courier_number].distance = orders[0].cords.get_distance(couriers[courier_number].cordsC)
for courier_number in range(len(couriers)):
    for courier_number in range(len(couriers)):
        if couriers[courier_number].distance == min(distances) and couriers[courier_number].load < orders[0].weight:
            distances.remove(min(distances))
        elif couriers[courier_number].distance == min(distances) and couriers[courier_number].load >= orders[0].weight:
            break
print(f"Заказ {orders[0].number} заберёт {couriers[courier_number].name}, расстояние {couriers[courier_number].distance}")
couriers[courier_number].cordsC = orders[0].cords

distances2 = []
for courier_number in range(len(couriers)):
    distances2.append(orders[1].cords.get_distance(couriers[courier_number].cordsC))
    couriers[courier_number].distance = orders[1].cords.get_distance(couriers[courier_number].cordsC)
for courier_number in range(len(couriers)):
    for courier_number in range(len(couriers)):
        if couriers[courier_number].distance == min(distances2) and couriers[courier_number].load < orders[1].weight:
            distances2.remove(min(distances2))
        elif couriers[courier_number].distance == min(distances2) and couriers[courier_number].load >= orders[1].weight:
            break
print(f"Заказ {orders[1].number} заберёт {couriers[courier_number].name}, расстояние {couriers[courier_number].distance}")
couriers[courier_number].cordsC = orders[1].cords

distances3 = []
for courier_number in range(len(couriers)):
    distances3.append(orders[2].cords.get_distance(couriers[courier_number].cordsC))
    couriers[courier_number].distance = orders[2].cords.get_distance(couriers[courier_number].cordsC)
for courier_number in range(len(couriers)):
    for courier_number in range(len(couriers)):
        if couriers[courier_number].distance == min(distances3) and couriers[courier_number].load < orders[2].weight:
            distances3.remove(min(distances3))
        elif couriers[courier_number].distance == min(distances3) and couriers[courier_number].load >= orders[2].weight:
            break
print(f"Заказ {orders[2].number} заберёт {couriers[courier_number].name}, расстояние {couriers[courier_number].distance}")
couriers[courier_number].cordsC = orders[2].cords

distances4 = []
for courier_number in range(len(couriers)):
    distances4.append(orders[3].cords.get_distance(couriers[courier_number].cordsC))
    couriers[courier_number].distance = orders[3].cords.get_distance(couriers[courier_number].cordsC)
for courier_number in range(len(couriers)):
    for courier_number in range(len(couriers)):
        if couriers[courier_number].distance == min(distances4) and couriers[courier_number].load < orders[3].weight:
            distances4.remove(min(distances4))
        elif couriers[courier_number].distance == min(distances4) and couriers[courier_number].load >= orders[3].weight:
            break
print(f"Заказ {orders[3].number} заберёт {couriers[courier_number].name}, расстояние {couriers[courier_number].distance}")
couriers[courier_number].cordsC = orders[3].cords

distances5 = []
for courier_number in range(len(couriers)):
    distances5.append(orders[4].cords.get_distance(couriers[courier_number].cordsC))
    couriers[courier_number].distance = orders[4].cords.get_distance(couriers[courier_number].cordsC)
for courier_number in range(len(couriers)):
    for courier_number in range(len(couriers)):
        if couriers[courier_number].distance == min(distances5) and couriers[courier_number].load < orders[4].weight:
            distances5.remove(min(distances5))
        elif couriers[courier_number].distance == min(distances5) and couriers[courier_number].load >= orders[4].weight:
            break
print(f"Заказ {orders[4].number} заберёт {couriers[courier_number].name}, расстояние {couriers[courier_number].distance}")
couriers[courier_number].cordsC = orders[4].cords

