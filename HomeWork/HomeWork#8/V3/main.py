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
