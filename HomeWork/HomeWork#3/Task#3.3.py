print(
    """
    3.Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
*Пример:*

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
    """
)

from random import uniform

# import uniform
# Этот метод возвращает вещественное число r такое, что x <= r < y.

n = int(input("Введите размер списка:  "))
list_1 = []
for i in range(n):
    f = uniform(0, 9)
    list_1.append(round(f, 2))

min_1 = list_1[0]
max_1 = 0
for i in range(len(list_1)):

    if max_1 < list_1[i]:
        max_1 = list_1[i]
    if min_1 > list_1[i]:
        min_1 = list_1[i]
dif = (max_1 - int(max_1)) - (min_1 - int(min_1))

print("Список: ", list_1)
print("Максимальное число: ", max_1, "Минимальное число: ", min_1)

print(round(dif, 2))

input("\n\nНажмите Enter чтобы выйти.")
