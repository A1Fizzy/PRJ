print("Введите номер студента:")
n = int(input())
if n <= 3:
    c = 3
    a = [0] * c
    print("Введите имя первого студента:")
    name1 = str(input())
    print("Введите его баллы:")
    for i in range(c):
        a[i] = int(input())
    b = [0] * c
    print("Введите имя второго студента:")
    name2 = str(input())
    print("Введите его баллы:")
    for i in range(c):
        b[i] = int(input())
    d = [0] * c
    print("Введите имя третьего студента:")
    name3 = str(input())
    print("Введите его баллы:")
    for i in range(c):
        d[i] = int(input())
    print("Список студентов и их баллы:")
    print(f"{name1} {a}")
    print(f"{name2} {b}")
    print(f"{name3} {d}")
    if n == 1:
        print(f"{name1} {sum(a) / 3}")
    elif n == 2:
        print(f"{name2} {sum(b) / 3}")
    elif n == 3:
        print(f"{name3} {sum(d) / 3}")
else:
    print("Количество студентов = 3")
