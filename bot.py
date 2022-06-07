import logging
from aiogram import Bot, Dispatcher, executor, types
from passwords import *
from categories import *
from dbrecords import insert_varible_into_table
from datetime_now import datetime_now
from functions import *

# Объект бота
bot = Bot(token=bot_token)
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# function to handle logs 
def input_logs(text_received, now, user_id):
    with open('input_logs.txt', 'a', encoding='utf-8') as output:
        print(f'{text_received}, {now}, {user_id}', file=output)

@dp.message_handler(commands="help")
async def cmd_test1(message: types.Message):
    await message.reply(f'ПРИМЕР ВВОДА: продукты 10.55 комментарий\n\nВыбери категорию из списка:\n\n{categories_str}\n\nКоманды: /help /last5 /statx ')

@dp.message_handler(commands="last5")
async def cmd_test1(message: types.Message):
    await message.reply(last5records(sql_query_expence_month(date_1(), date_2())))

@dp.message_handler(commands="statx")
async def cmd_test1(message: types.Message):
    await message.reply(f'Затраты в текущем месяце:\n\n{total_month_expences_by_category(sql_query_expence_month(date_1(), date_2()))}\n\nЗатраты в текущем месяце:\n{total_exepences(sql_query_expence_month(date_1(), date_2()))}\n\nЗатраты в текущем году:\n{total_exepences(sql_query_expence_month(month_1(), month_2()))}')        

@dp.message_handler(content_types=['text'])
async def add_expense(message: types.Message):
    if message.from_user.id not in [375857111, 5345727185]:  # проверяем валидность пользователя, 375857111 мой, 5345727185 Таня 
        return await message.reply(f'вы не авторизованы')
    else:
        try:
            text_received = message.text 
            mylist = text_received.split() 
            mylist[0] = mylist[0].lower()
            mylist2 = mylist.copy()
            mylist2.pop(0)
            mylist2.pop(0)
            comment_string = ' '.join(mylist2)  #строка с комментариями 

            if mylist[0] not in categories_list:
                with open('input_logs.txt', 'a', encoding='utf-8') as output:
                        print(f'{text_received}, {str(datetime.datetime.now())}, {message.from_user.id}', file=output)
                await message.reply(f'Ошибка!!! попробуй команду /help')

            if mylist[0] in categories_list:
                try: 

                    #ответ пользователю, дефольный сценарий 
                    if float(mylist[1]) > 0:
                        insert_varible_into_table(mylist[0], mylist[1], datetime_now(), comment_string, message.from_user.id)
                        await message.reply(f'добавлено! {mylist[0]}: {mylist[1]} EUR комментарий: ({comment_string})\ncтатистика: /statx')
                                            
                    #ответ пользователю при корректировке в минус 
                    elif float(mylist[1]) < 0:
                        insert_varible_into_table(mylist[0], mylist[1], datetime_now(), comment_string, message.from_user.id)
                        await message.reply(f'добавлено! {mylist[0]}: {mylist[1]} EUR комментарий: ({comment_string})\ncтатистика: /statx')

                    #ответ пользователю при нулевой стоимости     
                    elif float(mylist[1]) == 0:
                        input_logs(text_received, str(datetime_now()), message.from_user.id)
                        await message.reply(f'А чё НОЛЬ записывать?')

                except:
                    input_logs(text_received, str(datetime_now()), message.from_user.id)                   
                    await message.reply(f'Ошибка!!! попробуй команду /help')        
        
        except:
            input_logs(text_received, str(datetime_now()), message.from_user.id)
            await message.reply(f'Ошибка!!! попробуй команду /help') 

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)