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
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import *
from aiogram.dispatcher import FSMContext


logging.basicConfig(level=logging.INFO, filemode='a', filename='PyAiogram2bot.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')


TOKEN = TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью!')

@dp.message_handler(text='Calories')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)

    data = await state.get_data()
    callories = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 + int(data['age']) + 5

    await message.answer(f'Ваша норма калорий: {callories}')
    await state.finish()

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
