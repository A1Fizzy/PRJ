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

    def get_distance_to_center(self):
        x = self.x
        y = self.y
        R = math.sqrt(x**2 + y**2)
        return R


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

class Record:
    def __init__(self, name, point_from: Point, point_to: Point, time_start, time_finish):
        self.courier_name = name
        self.point_from = point_from
        self.point_to = point_to
        self.time_start = time_start
        self.time_finish = time_finish
        self.orders = []

    def __repr__(self):
        return f'Rec: имя: {self.courier_name}\n' \
               f'Rec: заказ {self.orders}\n' \
               f'Rec: от точки: {self.point_from}\n' \
               f'Rec: до точки {self.point_to}\n' \
               f'Rec: время старта {self.time_start}\n' \
               f'Rec: время финиша {self.time_finish}\n' \

class Courier:
    def __init__(self, name, cordsC, speed, load=10):
        self.name = name
        self.cordsC = cordsC
        self.speed = speed
        self.load = load
        self.distance = 0
        self.history = []

    def move(self, point_to, orders):
        point_from = self.cordsC
        time_start = 0
        if self.history:
            last_rec = self.history[-1]
            point_from = last_rec.point_to
            time_start = last_rec.time_finish

        dist = point_from.get_distance(point_to)
        duration = dist / self.speed
        time_finish = time_start + duration
        rec = Record(self.name, point_from, point_to, time_start, time_finish)
        rec.orders = orders
        self.history.append(rec)

    def __str__(self):
        return f'{self.name}с координатами {self.cordsC} имеет скорость {self.speed} км/ч и грузоподъёмность {self.load} кг'


c1 = Courier('Курьер 1 (пеший)', pc1, 6, 2)
c2 = Courier('Курьер 2 (пеший)', pc2, 6, 2)
c3 = Courier('Курьер 3 (на велосипеде)', pc3, 12, 4)
c4 = Courier('Курьер 4 (на велосипеде)', pc4, 12, 4)
c5 = Courier('Курьер 5 (на автомобиле)', pc5, 60, 50)

plan = {'Курьер 1': [Order('A', p1, 2), Order('B', p2, 3)], 'Курьер 2': [Order('C', p3, 1), Order('D', p4, 6)]}

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

for i in range(len(orders)):
    print(orders[i])
print("\n")
for j in range(len(couriers)):
    print(couriers[j])
print("\n")
arr = []
for order_number in range(len(orders)):
    distances = []
    for courier_number in range(len(couriers)):
        distances.append(orders[order_number].cords.get_distance(couriers[courier_number].cordsC))
        couriers[courier_number].distance = orders[order_number].cords.get_distance(couriers[courier_number].cordsC)
    for courier_number in range(len(couriers)):
        for courier_number in range(len(couriers)):
            if couriers[courier_number].distance == min(distances) and couriers[courier_number].load < orders[order_number].weight:
                distances.remove(min(distances))
            elif couriers[courier_number].distance == min(distances) and couriers[courier_number].load >= orders[order_number].weight:
                couriers[courier_number].cordsC = orders[order_number].cords
                full_path = orders[order_number].cords.get_distance_to_center() + couriers[courier_number].distance
                time = full_path / couriers[courier_number].speed
                time_to_order = couriers[courier_number].distance / couriers[courier_number].speed
                arr.append(f"Заказ {orders[order_number].number} заберёт {couriers[courier_number].name}, доставит в течение {time} часов, расстояние {full_path} км")
for i in set(arr):
    print(i)
"""
class Image:
    def __init__(self, time_finish, Point1, Point2):
        self.time_start = 0
        self.time_finish = time_finish
        self.point_from = Point1
        self.point_to = Point2


    def __str__(self):
        return f'время начала: {self.time_start} \nвремя финиша: {self.time_finish} \nот {self.point_from} \nдо {self.point_to}'


courier_list = Record(couriers[courier_number].name, orders[order_number].number, couriers[courier_number].cordsC, orders[order_number].cords, 0, 10)
print(courier_list)
"""


