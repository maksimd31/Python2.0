# 1 По двум заданным числам проверить является ли одно квадратом второго.
print('1. По двум заданным числам проверить является ли одно квадратом второго.')

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

if a ** 2 == b:  # Введеное число возводится в вторую степень и сравнивается с вторым числом.
    print('Второе квадрат первого')
elif b ** 2 == a:
    print('Первое квадрат второго')
else:  # Если не подходят варианты
    print('Числа не является квадратом другого')
