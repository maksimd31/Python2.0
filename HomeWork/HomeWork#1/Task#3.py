# 3 Вывести на экран числа от -N до N.

print('# 3 Вывести на экран числа от -N до N.')

number = int(input(" Введите число : "))

number_two = number * -1

for i in range(number_two, number + 1):  # Пробежка по циклу
    print(i)
