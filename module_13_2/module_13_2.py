from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='AiogramBot.txt',
                    format='%(asctime)s | %(levelname)s | %(message)s')


TOKEN = ''

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())




if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates=True)
    except:
        print('Ошибка!')
        logging.warning('Ошибка', exc_info=True)