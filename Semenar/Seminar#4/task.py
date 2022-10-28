import sqlite3 
 
bd= sqlite3.connect("Data_base.db") 
 
cursor = bd.cursor() 
 
cursor.execute('''CREATE TABLE IF NOT EXISTS personal( 
    id INTEGER PRIMARY KEY autoincrement, 
    name TEXT, 
    last_name TEXT, 
    position TEXT, 
    salary INT, 
    bonus INT 
)''') 
 
 
baza=[(1,"Иван","Иванов","главный инженер",50000,10000), 
(2,"Игорь","Семенов"," инженер",20000,8000), 
(3,"Олег","Петров","завхоз",12000,3000)] 
 
try: 
    cursor.executemany('INSERT INTO personal VALUES(?,?,?,?,?,?)',baza) 
    bd.commit() 
except: 
    print('Данные уже есть') 
 
 
for i in cursor.execute('SELECT * FROM personal'): 
    print(*i) 
 
# cursor.execute('DELETE from personal WHERE id=1') 
 
# cursor.execute('select * from personal WHERE name LIKE "Олег";') 
# one= cursor.fetchmany() 
# print(*one) 
 
cursor.execute('select * from personal WHERE id=2;') 
one= cursor.fetchone() 
print(one) 
 
 
 
 
 
 
def previev_base(): 
    for i in cursor.execute('SELECT * FROM personal'): 
        print(*i) 
 
 
def add_record(): 
    pass 
 
def find_record(column,nam): 
    cursor.execute(f'select * from personal WHERE {column} LIKE {nam};') 
    one= cursor.fetchmany() 
    return one 
 
def delete_record(id): 
    cursor.execute(f'DELETE from personal WHERE id={id}') 
    bd.commit() 
 
 
# for i in cursor.execute('SELECT * FROM personal'): 
#     print(*i) 
 
 
def input_choice(): 
 
    while True: 
        user_choice= input('1- просмотреть базу:,2- добавить запись:, 3- удалить запись:,4- найти по Ф.И.О:, q- выход:') 
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
 
                   
 
 
cursor.execute('UPDATE personal SET salary = 55000 WHERE id=2;') 
bd.commit() 
 
for i in cursor.execute('SELECT * FROM personal'): 
    print(*i)