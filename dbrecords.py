import sqlite3

# func to handle database records 
def insert_varible_into_table(category, expence, datetime, comments, user_id):
    try:
        sqlite_connection = sqlite3.connect('mydatabase.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_insert_with_param = """INSERT INTO costs
                              (category, expence, datetime, comments, user_id)
                              VALUES (?, ?, ?, ?, ?);"""

        data_tuple = (category, expence, datetime, comments, user_id)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqlite_connection.commit()
        print("Переменные Python успешно вставлены в таблицу costs")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")



