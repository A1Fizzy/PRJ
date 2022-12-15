import math
print("Введите количество точек:")
N = int(input())
pointx = []
pointy = []
for i in range(N):
    print("Введите точку",i,':')
    x = int(input())
    y = int(input())
    pointx.append(x)
    pointy.append(y)
max = 0
min = 0
for i in range(len(pointx) -1):
    distance = math.dist((pointx[i],pointy[i]),(pointx[i+1],pointy[i+1]))

    if distance < min:
        min = distance
    elif distance > max:
        max = distance
        x1 = pointx[i]
        y1 = pointy[i]
        x2 = pointx[i+1]
        y2 = pointy[i+1]
print(f'Минимальное расстояние между точками ({x1},{y1}) and ({x2},{y2}) : {min}')
print(f'Максимальное расстояние между точками ({x1},{y1}) and ({x2},{y2}) : {max}')