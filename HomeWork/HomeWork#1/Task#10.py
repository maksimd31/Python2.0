# 10 Найти расстояние между двумя точками пространства.

x1 = float(input('Введите x1: '))
y1 = float(input('Введите y1: '))
x2 = float(input('Введите x2: '))
y2 = float(input('Введите y2: '))
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print('Расстояние между точками = ', round(distance, 2))

from random import random

numbers = []
for j in range(6):
    numbers.append(int(random() * 6))
print(numbers)
numbers = sorted(numbers)
