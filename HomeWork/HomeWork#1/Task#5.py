# 5 Дано число. Проверить кратно ли оно 5 и 10 или 15, но не 30

print('5 Дано число. Проверить кратно ли оно 5 и 10 или 15, но не 30')
number_four = int(input("Введите число :"))

if (number_four % 5 == 0 and number_four % 10 == 0 or number_four % 15 == 0) and number_four % 30 != 0:
    print("Кратно")
else:
    print("Не кратно")
