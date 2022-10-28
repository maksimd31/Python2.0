# типы данных и пременных
# int, float, boolean, str, list, None

#value = None
#print(type(value))
#a = 123
#b = 1.23
#print(type(a))
#print(type(b))
#value = 12334
#print(type(value))
#s = 'hello world'
#print(s) #вывод строки
#print(a, '-', b, '-',  s)
#print('{1} - {2} - {0}'.format(a, b, s))
#print(f'{a} - {b} - {s}')

#f = False
#print(f)

#list = ['1', '2', '3']
#col = ['hello', 1, 2, 4.5, True]
#print(list)
#print(col)


# Ввод и вывод данных
# print, input

#print('Введите a');
#a = float(input())
#print('Введите b');
#b = float(input())
#print(a, '+', b, '=', a + b)
# print ('{} {}'.format(a, b))
# print(f'{a} {b}')

# Арифметические операции
# +, -, *, /, %, //, **
# (), Сокращенные операции
# / по умолчанию равно вещественному число
# // деление с целым результатом
# ** возведение в степень

#a = 1.3
#b = 3
#c = round(a * b, 5)
#print(c)
#a += 5
#print(a)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen

#a = 'qwe'
#b = 'qwe'
#print(a == b)

#a = 1 < 3 <4
#print(a)

#func = 1
#T = 4
#x = 2
#print(func<T>(x))

#f = 1 > 2 or 2 < 4
#print(f)

#f = [1, 2, 3, 4]
#print(f)
#print(2 in f)

#is_odd = not f[0] % 2
#print(is_odd)

# Управляющие конструкции
# if, if-else

#a = int(input('a = '))
#b = int(input('b = '))
#if a > b:
#    print(a)
#else:
#    print(b)

#username = input('Введите имя: ')
#if username == 'Оля':
#    print('Ура! Это же Оля')
#elif username == 'Вика':
#    print('Я так ждала Вас, Вика')
#elif username == 'Серегей':
#    print('Сергей - топ')
#else:
#    print('Привет, ', username)

# Управляющие конструкции
# while

#original = 23
#inverted = 0
#while original != 0:
#    inverted = inverted * 10 + (original % 10)
#    original //= 10
#    print(original)
#else:
#    print('Пожалуй')
#    print('хватит )')
#print(inverted)

# Управляющие конструкции
# for

#for i in 1, 2, 3, 4, 5:
#    print(i**2)

#list = [1, 2, 3, 4, 10, 5]
#for i in list:
#    print(i)

#r = range(10)
#for i in r:
#    print(i)

#for i in range(1, 10, 2):
#    print(i)

#for i in 'qwe - rty':
#    print(i)

# строки

#text = 'съешь еще этих мягких французских булок'
#print(len(text))                        # 39
#print('еще' in text)                    # True
#print(text.isdigit())                   # False
#print(text.islower())                   # True
#print(text.replace('еще', 'ЕЩЕ'))       #  

#for c in text:
#    print(c)

#help(text.istitle)

#text = 'съешь еще этих мягких французских булок'
#print(text[0])                            # с
#print(text[1])                            # ъ
#print(text[len(text)])                    # IndexError
#print(text[len(text) - 1])                # к
#print(text[-5])                            # б
#print(text[:])                            # print(text)
#print(text[:2])                            # съ
#print(text[len(text) - 2:])               # ок    
#print(text[2:9])                          # ешь еще
#print(text[6:-18])                        # еще этих мягких
#print(text[0:len(text):6])                # сеикакл 
#print(text[::6])                          # сеикакл 
#text = text[2:9] + text[-5] + text[:2]    # ... 
#print(text)

# Списки list

#numbers = [1, 2, 3, 4, 5]
#print(numbers)
#ran = range(1, 6)
#print(type(ran))
#numbers = list(ran)
#print(type(numbers))
#print(numbers)
#numbers[0] = 10
#print(f'{len(numbers)} len')
#print(numbers)
#for i in numbers:
#    i *= 2
#    print(i)
#print(numbers)

#colors = ['red', 'green', 'blue']

#for e in colors:
#    print(e)                # red green blue

#for e in colors:
#    print(e*2)              # redred greengreen blueblue

#colors.append('gray')       # добавить в конец
#print(colors == ['red', 'green', 'blue', 'gray'])   # True
#colors.remove('red')        # del colors[0] удалить элемент


def f(x):
    if x == 1:
      return 'Целое'
    elif x == 2.3:
       return 23
    else:
               return  

arg = 2.3
print(f(arg))
print(type(arg))

