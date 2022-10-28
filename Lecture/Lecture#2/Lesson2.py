# with open('file.txt', 'a') as data:
#     data.write('line 1111\n')
#     data.write('line 2222\n')



# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.write('LINE 12\n')
# data.write('LINE 13\n')
# data.close()


# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

def new_string(symbol, count = 3):
    return symbol * count

print(new_string('!', 5))   # !!!!!
print(new_string('!'))         #!!!
print(new_string(4))           #12




def concatenatio(*params):
    res = 0 # res: str = "" для строки
    for item in params:
        res += item
    return res

# print(concatenatio('a', 's', 'd', 'w'))  # asdw
# print(concatenatio('a', '1', 'd', '2'))  # a1d2
print(concatenatio(1, 2, 3, 4))  # TypeError:...


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n -2)

list = []
for e in range(1, 10):
    list.append(fib(e))
print(list)  # 1 1 2 3 5 8 13 21 34

a = (3, 1, 41, 4)  # кортеж - неизменяемый список (3,) для единичного элемента
# print(a)
# print(a[-2])

for item in a:
    print(item)

t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue))  # r:red g:green b:blue

# Словари 
# Неупорядоченные коллекции произвольных переменных объектов с доступом по ключу

dictionary = {}
dictionary = \
    {
        'up': '↑',
        'left': '←',
        'down': '↓',
        'right': '→'
    }
print(dictionary) # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary['left']) # ←


for k in dictionary.keys():
    print(k)

for v in dictionary:
    print(dictionary[v])

print(dictionary['up'])  # ↑
# типы ключей могут отличаться

dictionary['left'] = '←'
print(dictionary['left']) # ←
# print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента

for item in dictionary: # for (k,v) in dictionary.items():
    print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →



