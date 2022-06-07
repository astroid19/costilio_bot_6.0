import sqlite3
from datetime import datetime
from categories import *


# функция формирующая даты для SQL выборки текущий месяц
def date_2() -> str:
    now = datetime.now()
    now_list = list(now.strftime("%Y-%m-%d"))
    # в текущей дате заменяем текущее число на 1
    now_list[9] = '1'
    # в текущем месяце заменяем на + 1
    now_list[6] = str(int(now_list[6]) + 1)
    date_2 = ''.join(now_list)
    print(date_2)
    return date_2


# функция формирующая даты для SQL выборки текущий месяц
def date_1()-> str:
    # в текущей дате заменяем текущее число на 1
    now = datetime.now()
    now_list = list(now.strftime("%Y-%m-%d"))
    now_list[9] = '1'
    #now_list[6] = str(int(now_list[6]))
    date_1 = ''.join(now_list)
    print(date_1)
    return date_1

# функция формирующая даты для SQL выборки текущий год
def month_2() -> str:
    now = datetime.now()
    now_list = list(now.strftime("%Y-%m"))
    # в текущем месяце заменяем на + 1
    now_list[-1] = str(int(now_list[6]) + 1)
    month_2 = ''.join(now_list)
    print(month_2)
    return month_2

# функция формирующая даты для SQL выборки текущий год
def month_1() -> str:
    now = datetime.now()
    now_list = list(now.strftime("%Y-%m"))
    # в текущем месяце заменяем на 1
    now_list[-1] = '1'
    month_1 = ''.join(now_list)
    print(month_1)
    return month_1


# sqlite3 запрос выбирает всю базу за период в месяц / год
def sql_query_expence_month(date_1, date_2) -> list: 
    sqlite_connection = sqlite3.connect('mydatabase.db')
    cursor = sqlite_connection.cursor()
    print("Подключен к SQLite")

    sqlite_select_query = """SELECT category, expence
                                    FROM costs 
                                    WHERE datetime BETWEEN ? AND ?
                                    """
    cursor.execute(sqlite_select_query, (date_1, date_2))
    records = cursor.fetchall()
    print(records)
    print('\n\n')
    return records
    cursor.close()
#sql_query_expence_month(date_1(), date_2())
#sql_query_expence_month(month_1(), month_2())


# list records_list == сумма затрат за месяц по даннной категории 
def total_month_expences_by_category(records: list) -> str:
    records_list = []
    for c in categories_list:
        caregory_sum = 0
        caregory_sum_str = ''
        for i in records:
            if c == i[0]:
                caregory_sum += i[1]
        caregory_sum = round(caregory_sum, 2)
        caregory_sum_str = c + ' '  + str(caregory_sum) + ' EUR' + '\n'
        records_list.append(caregory_sum_str)
    records_str = ''.join(records_list)
    print(records_str)
    return records_str
#total_month_expences_by_category(sql_query_expence_month(date_1(), date_2()))

# int total_records_sum == сумма всего за месяц / год
def total_exepences(records: list) -> str:
    total_records_sum = 0
    for i in records:
        total_records_sum += i[1]
    total_records_sum = round(total_records_sum, 2)
    print(total_records_sum)
    total_records_sum_str = str(total_records_sum) + ' EUR'
    return total_records_sum_str
#total_exepences(sql_query_expence_month(date_1(), date_2()))
#total_exepences(sql_query_expence_month(month_1(), month_2()))

# возвращает 5ть последних записей из базы
def last5records(records: list) -> str:
    last5records_str = str(records[-5]) + '\n' + str(records[-4]) + '\n' + str(records[-3]) + '\n' + str(records[-2]) + '\n' + str(records[-1]) + '\n'
    print(last5records_str)
    return last5records_str
#last5records(sql_query_expence_month(date_1(), date_2()))




if __name__ == "__main__":

    print(f'# list records_list == сумма затрат за месяц по даннной категории')
    total_month_expences_by_category(sql_query_expence_month(date_1(), date_2()))
    
    print(f'# list records_list == сумма затрат за год по даннной категории')
    total_month_expences_by_category(sql_query_expence_month(month_1(), month_2()))

    print(f'# int total_records_sum == сумма всего за месяц {total_exepences(sql_query_expence_month(date_1(), date_2()))}')
    
    print(f'# int total_records_sum == сумма всего за месяц {total_exepences(sql_query_expence_month(month_1(), month_2()))}')
    
    print(f'Последние 5ть затрат:\n{last5records(sql_query_expence_month(date_1(), date_2()))}')    