# Доделать решение задачи: Задача: Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы

### Я пытался улучшить эти сущности изучая встроенный модуль sqlite3 
### Версия №1 исправно работает 
### Версия №2 с использованием with / что бы избежать постоянный ввод bd.commit()
### Версия №3 (не понял как исправить ошибку ввода и ограничений вода при одинаковых данных и возвратом в начало ввода функции)

## Версия №1 
```py
import sqlite3
from sqlite3 import Error



# NULL — значение NULL
# INTEGER — целое число можно записать int
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
    cursor.execute('''INSERT INTO personal(name, last_name, position, salary,bonus) VALUES (?, ?, ?, ?,?)''', (name, last_name, position, salary,bonus))
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

```
## Версия №2 с использованием with / что бы избежать постоянный ввод bd.commit()
```py
import sqlite3
# соединение с базой данных
with sqlite3.connect('Data_Base.db') as db:
    cursor = db.cursor()
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS personal(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        last_name TEXT,
        position TEXT,
        salary INT,
        bonus INT
    )""")

    baza = [
        ("Иван", "Иванов", "главный инженер", 50000, 10000),
        ("Игорь", "Семенов", " инженер", 20000, 8000),
        ("Олег", "Петров", "завхоз", 12000, 3000)
    ]
    cursor.executemany(
        "INSERT INTO personal(name,last_name,position,salary,bonus) VALUES(?,?,?,?,?)",
        baza)  # позволяет заносить данные одновременно

    # cursor.execute("SELECT * FROM personal")  # Выводим данные таблицы
    # print("\n", cursor.fetchall(), "\n")  # выводит всю базу данных
    # cursor.fetchone()#Выводит первую строку
    # cursor.fetchmany(2)#выводит количество заданных строк
    # cursor.fetchmany()

    for data in cursor.execute("SELECT * FROM personal"):
        print(data)

```
## Версия №3 (не понял как исправить ошибку ввода и ограничений вода при одинаковых данных и возвратом в начало ввода функции)
```py
import sqlite3
# соединение с базой данных
with sqlite3.connect('Data_Base.db') as db:  # конструкция позволит избежать db.commit()
    cursor = db.cursor()

    qwert = """
    CREATE TABLE IF NOT EXISTS personal(
        id INTEGER PRIMARY KEY,
        login TEXT
        name TEXT,
        last_name TEXT,
        position TEXT,
        salary INT,
        bonus BIGINT NOT NULL DEFAULT 5000
    )
    """

    cursor.executescript(qwert)  # позволяет массово заносить данные

print('Заполните карточку сотрудника')


def REGIS():
    login = input("Введите логин: ")
    name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    position = input("Введите должность: ")
    salary = input("Введите зарплату: ")
    # bonus = input("Введите зарплату: ")

    try:
        db = sqlite3.connect("Data_Base.db")
        cursor = db.cursor()

        cursor.execute("SELECT login FROM personal WHERE login = ?", [login])
        if cursor.fetchone() is None:
            baza = [login, name, last_name, position, salary]
            cursor.execute("INSERT INTO personal(login,name,Last_name,position,salary) VALUES(?,?,?,?,?,)", baza)
            db.commit()
    except:
        print('Такой логин уже зарегистрирован')
        REGIS()
    finally:
        cursor.close()
        db.close()

REGIS()
```
