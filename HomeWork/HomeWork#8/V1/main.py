import sqlite3
from sqlite3 import Error

# NULL — значение NULL
# INTEGER — целое число
# REAL — число с плавающей точкой
# TEXT — текст
# BLOB — бинарное представление крупных объектов, хранящееся в точности с тем, как его ввели

BD = sqlite3.connect("Base_Date.db")

# cursor. Он позволяет делать SQL-запросы к базе. Используем переменную cur для хранения объекта

cursor = BD.cursor()

# Функция execute отвечает за SQL-запрос
# Первая таблица
# cur.execute - запрос для создания таблиц
cursor.execute('''CREATE TABLE IF NOT EXISTS personal( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT, 
    last_name TEXT, 
    position TEXT, 
    salary INT, 
    bonus INT 
)''')
BD.commit()  # сохранить таблицы

# baza = [(input('введите данные через пробел: '))]

baza = [("Иван", "Иванов", "главный инженер", 50000, 10000),
        ("Игорь", "Семенов", " инженер", 20000, 8000),
        ("Олег", "Петров", "завхоз", 12000, 3000)]

# Вставляем данные в таблицу
try:
    # cur.executemany('INSERT INTO personal VALUES(?,?,?,?,?,?)', baza)
    cursor.executemany("INSERT INTO personal VALUES(?,?,?,?,?)", baza)
    BD.commit()
except:
    print('Данные уже есть')


# for i in cursor.execute('SELECT * FROM personal'):
#     print(*i)

def input_choice():
    while True:
        user_choice = input(
            '1- просмотреть базу: \n2- добавить запись: \n3- удалить запись: \n4- найти по Ф.И.О: \nq- выход: \nВвод данных: ')
        if user_choice == "1":
            previev_base()
        elif user_choice == "2":
            add_record()
        elif user_choice == "3":
            delete_record()
        elif user_choice == "4":
            find_record()
        elif user_choice == "q":
            print('Выход')
            break
        else:
            print('Не верно введен режим работы')


def previev_base():
    for i in cursor.execute('SELECT * FROM personal'):
        print(*i)


def add_record():
    # Вводим данные
    name = input('Введите имя: ')
    last_name = input('введите фамилию: ')
    position = input('Введите должность: ')
    salary = input('Введите зарплату: ')
    bonus = input('введите бонус: ')
    # Вставляем данные
    cursor.execute('''INSERT INTO personal(name, last_name, position, salary,bonus) VALUES (?, ?, ?, ?,?)''',
                   (name, last_name, position, salary, bonus))
    BD.commit()
    # Сохраняем изменения
    BD.commit()


def find_record(name, last_name):
    cursor.execute(f'select * from personal WHERE {name} LIKE {last_name};')
    one = cursor.fetchmany()
    return one


def delete_record(id):
    cursor.execute(f'DELETE from personal WHERE id={id}')
    BD.commit()


input_choice()
