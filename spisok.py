print("Введите список родственников со стороны Полины:")
n = 1000
spisok_polina = {}
for i in range(n):
    name = str(input())
    end = str('конец')
    if name == end:
        break
    else:
        v1 = int(input())
        spisok_polina[name] = v1
total_polina = sum(spisok_polina.values())
print("Всего родственников со стороны Полины:")
print(total_polina, "\n")

print("Введите список родственников со стороны Артёма:")
n = 1000
spisok_artem = {}
for i in range(n):
    name = str(input())
    end = str('конец')
    if name == end:
        break
    else:
        v1 = int(input())
        spisok_artem[name] = v1
total_artem = sum(spisok_artem.values())
print("Всего родственников со стороны Артёма:")
print(total_artem, "\n")
print("Всего родственников:")
print(total_artem + total_polina)