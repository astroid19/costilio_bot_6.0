import sqlite3

try:
    sqlite_connection = sqlite3.connect('mydatabase.db')
    sqlite_create_table_query = '''CREATE TABLE costs (
                                category TEXT NOT NULL,
                                expence REAL NOT NULL,
                                datetime DATETIME NOT NULL,
                                comments TEXT,  
                                user_id INTEGER);'''

    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print("Таблица SQLite создана")

    cursor.close()

except sqlite3.Error as error:
    print("Не удалось вставить данные в таблицу sqlite")
    print("Класс исключения: ", error.__class__)
    print("Исключение", error.args)
    print("Печать подробноcтей исключения SQLite: ")
    exc_type, exc_value, exc_tb = sys.exc_info()
    print(traceback.format_exception(exc_type, exc_value, exc_tb))
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")