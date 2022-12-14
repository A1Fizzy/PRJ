print("Введите количетво студентов:")
n = int(input())
s = {}
print("Введите имя и баллы студента:")
for i in range(n):
    a = str(input())
    values = int(input())
    values1 = int(input())
    values2 = int(input())
    s[a] = values, values1, values2
print("Список студентов:")
print(s)
for i in range(n):
    print("Введите имя студента, средний балл которого хотите узнать:")
    name = s.get(str(input()))
    print(f"Средний балл: {sum(name) / 3}")
