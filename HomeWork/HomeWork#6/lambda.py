# lambda -Python-лямбды — это маленькие анонимные функции, подчиняющиеся более строгому, но более лаконичному синтаксису, чем обычные функции Python.
# Сокращение — это стратегия лямбда-исчисления

incoming_text = 'абвлабфбв слияние абвцукв текста алоабвабв выполнено'


def del_words(incoming_text):
    incoming_text = list(filter(lambda x: 'абв' not in x, incoming_text.split()))
    return " ".join(incoming_text)


incoming_text = del_words(incoming_text)
print(incoming_text)


# https://telegra.ph/Lambda-funkciya-10-15 - моя шпаргалка которую я написал

# Пример lambda
# к примеру используем обычную функцию, которая рассчитывает площадь прямоугольника.
def rect(a, b):
    return a * b


print('Площадь прямоугольника: ', rect(17, 14))
# Пример с использованием lambda (в одну строку)
print((lambda a, b: a * b)(17, 14))

print('- ' * 40)  # Разделитель


# к примеру используем обычную функцию, которая рассчитывает большее из двух чисел
def maxi(a, b):
    if a > b:
        return a
    else:
        return b


print(maxi(23, 17))

# Пример с использованием lambda (в одну строку)
print((lambda a, b: a if a > b else b)(23, 17))

a = input('Введите число: ')
numbers_list = a
result_list = list(filter(lambda a: numbers_list.count(a) == 1, numbers_list))
print(f'Для последовательности {numbers_list}, \n   список уникальных элементов => {result_list}')
