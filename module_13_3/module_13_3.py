####################################################################################################################
#
#   Нужно открыть папку с установленными пакетами, найти там папки: (Lib - site-packages - aiogram - bot)
#
#   Там будут 2 файла - это api.py и base.py.
#
#   В base.py найди строку
#       async with session.get(url, timeout=timeout, proxy=self.proxy, proxy_auth=self.proxy_auth) as response
#   и вставь в параметры ssl=False.
#
#   А в файле api.py - найди строку
#       async with session.post(url, data=req, **kwargs) as response
#   и аналогичным образом добавь в парамеры ssl=False.
#
####################################################################################################################


from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
import asyncio
from config import *

logging.basicConfig(level=logging.INFO, filemode='w', filename='PyAiogram2bot.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')


TOKEN = TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью!')

@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    try:
        logging.info('Запуск PyAiogram2bot!')
        executor.start_polling(dp, skip_updates=True)
        logging.info('PyAiogram2bot остановлен!')
    except:
        print('Ошибка запуска PyAiogram2bot!')
        logging.warning('Ошибка запуска PyAiogram2bot!', exc_info=True)
