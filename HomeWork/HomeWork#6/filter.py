# filter()

def f(x):
    return x > 10


a = [14, 0, 4, 6, 22, 66, 44, 222, 3665, 5, 8, 444]
b = list(filter(f, a))
print(b)

# список чисел
# filter() работает только с списками
numbers = [1, 2, 4, 5, 7, 8, 10, 11]


# функция, которая проверяет числа
def f(n):
    if (n % 2) == 0:
        return True
    else:
        return False


# Применение filter() для удаления нечетных чисел
out_filter = filter(f, numbers)

print("Отфильтрованный список: ", list(out_filter))

#тоже самое
print(list(filter(lambda x: (x % 2) == 0, numbers)))
