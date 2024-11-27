from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
import asyncio
from config import *

logging.basicConfig(level=logging.INFO, filemode='w', filename='AiogramBot.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью!')

@dp.message_handler()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')



if __name__ == '__main__':
    try:
        logging.info('AiogramBot запущен!', exc_info=True)
        executor.start_polling(dp, skip_updates=True)
        logging.info('AiogramBot остановлен!', exc_info=True)
    except:
        print('Ошибка запуска AiogramBot!')
        logging.warning('Ошибка запуска AiogramBot!', exc_info=True)
