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
