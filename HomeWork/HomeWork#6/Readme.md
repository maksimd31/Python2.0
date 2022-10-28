 ```py
 ( ( .          ) )      (     ( .        (          (    
 )\)\  (  ( (  (\(       )\    )\  (  (   )\         )\   
(_)(_) )\ )\)\  )(|     ((_)  ((() )\ )\ ((_)       ((_)  
| || |((_)_((_) ()\     \ \    / /((_)( )| |__     (/ /   
| __ | _ \ '  \/ -_)     \ \/\/ // _ \ '_| / /     / _ \  
|_||_|___/_|_|_|___|      \_/\_/ \___/_| |_\_\     \___/  
```


С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

## больше конечно меня заинтересовали последние 2 семинара 

1. lambda

```py

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

```

2. filter

```py
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

```

3. map
```py
# map - Python map() — это встроенная функция, которая позволяет обрабатывать и преобразовывать все элементы в итерируемом объекте без использования явного цикла for, методом, широко известным как сопоставление (mapping). map() полезен, когда вам нужно применить функцию преобразования к каждому элементу в коллекции или в массиве и преобразовать их в новый массив.

# список
# встроенные функции
# abs - меняет - на + и на оборот 
# map - может заменить for

a = [-1, 2, -3, 4, 5]
print(list(map(abs, a)))


def f(x):
    return x ** 2


a = [1, 2, 3, 5, 6, 7, 8, 9, 0]
print(list(map(f, a)))

a = [1, 2, 3, 4, 5, 67, 8, 9, 9]
vv = []


def ff(x):
    return x ** 2


for x in a:
    vv.append(ff(x))

print(vv)

# #вариант через map
vv = list(map(ff, a))
print(vv)

# with open('27.txt', 'r', encoding='utf-8') as f:
#     n = int(f.readline())
#     for i in range(n):
#         a, b = map(int, f.readline().split())
#         print(a, b)

# не работает
# я пытаюсь считать с файла данные цифры вытащить и сложить их
with open('27.txt') as f:
    n = int(f.readline())
    for i in range(n):
        a, b = map(int, f.readline().split())  # через map преобразовали str в int
        print(a + b)


# еше варианты с строками
def upper(string):
    return string.upper()


listt = ['FeeAes', 'eseRese', 'seTREsese', 'seseseEFGESesea']

print(list(map(upper, listt)))
print([string.upper() for string in listt])
# print(list(map(lambda string: string.upper(listt))))
print(list(map(lambda string: string.upper(), listt)))


def lowerr(string):
    return string.lower()


print(list(map(lowerr, listt)))
print([string.lower() for string in listt])
print(list(map(lambda string: string.lower(), listt)))


def stripp(string):
    return string.strip()


print(list(map(stripp, listt)))
print([string.strip() for string in listt])
print(list(map(lambda string: string.strip(), listt)))

```
4. zip
```py
# zip создает кортежи стоящие на одинаковых индексах
# через zip нельзя вызавть len а также вызвать индекс
# zip можно итерировать только один раз

# есть два списка
a = [5, 6, 7, 8, 9]

b = [100, 200, 300, 30, 65]

c = 'sdsd', 'sdsdd', 'sdsdsd', 'sdwedwse', 'sdsdsdcf'

d = 'ABCDF'

# for i in range(5):
#     print(a[i], b[i])

print(list(zip(a, b, c, d)))

# массовое присвоение через zip

for a1, b1, c1, d1 in zip(a, b, c, d):
    print(a1, b1, c1, d1)

# Получение списков через zip. сортирует по спискам

result = zip(a, b, c, d)

a2, b2, c2, d1 = zip(*result)
print(a2, b2, c2, d1)

# print(a2,b2,c2,d1 = zip(*result))

# * - выполняет распаковку элементов


```
5. enumerate
```py
# enumerate() 
# Синтаксис функции enumerate() выглядит следующим образом:
# enumerate(iterable, start)
# Функция enumerate() принимает два параметра: iterable и start.

# iterable — это итерируемый объект (список, кортеж и т.д.), который будет возвращен в виде пронумерованного объекта (объекта enumerate)

# start — это начальный индекс для возвращаемого объекта enumerate. Значение по умолчанию равно 0, поэтому, если вы опустите этот параметр, в качестве первого индекса будет использоваться 0.

a = ['14', '0', '4', '6', '22', '66', '44', '222', '3665', '5', '8', '444']
b = [14, 0, 4, 6, 22, 66, 44, 222, 3665, 5, 8, 444]
e = enumerate(a)
c = enumerate(b)

print(list(e))
print('-' * 40)
print(list(c))


```
6. list comprehension

```py

# list_comprehension

# def f (x):
#     return x>9 and x<100

# a = [14,0,4,6,22,66,44,222,3665,5,8,444]
# b = [i for i in a if i>9 and i<100]
# print(b)

# пример к следующему д/з

people = [{
    "first_name": "Василий",
    "last_name": "Марков",
    "birthday": "9/25/1984"
}, {
    "first_name": "Регина",
    "last_name": "Павленко",
    "birthday": "8/21/1995"
}]

birthdays = [
    person[term]
    for person in people
    for term in person
    if term == "birthday"
]

print(birthdays)

# В этом примере мы сперва перебираем people, присваивая каждый словарь person. После этого перебираем каждый идентификатор в словаре, присваивая ключи term. Если значение term равно birthday, то значение person[term] добавляет в list comprehension.

```
