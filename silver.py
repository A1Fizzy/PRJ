print("Введите кол-во финалистов:")
n = int(input())
print("Введите результаты финалистов:")
from itertools import groupby
A = [0] * n
for i in range(n):
    A[i] = int(input())
#print(A)
new_A = [el for el, _ in groupby(A)]
new_A.sort()
#print(new_A)
c = len(new_A)
print("Баллы у первого места:")
print(new_A[c-1])
print("Баллы у второго места:")
print(new_A[c-2])
print("Баллы у третьего места:")
print(new_A[c-3])

