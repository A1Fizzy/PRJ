print("Введите количество студентов:")
n = int(input())
spisok = {}
for i in range(n):
    print("Введите имя и баллы студента:")
    name = str(input())
    v1 = int(input())
    v2 = int(input())
    v3 = int(input())
    spisok[name] = v1, v2, v3
print(spisok, "\n")
arr = []
for i in spisok:
    a = sum(spisok[i]) / 3
    arr.append(a)
names = []
for i in spisok:
    names.append(i)
print("Наибольший средний балл у:")
print(f"{names[arr.index(max(arr))]} {max(arr)}")