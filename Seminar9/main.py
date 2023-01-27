from aiogram import Bot, Dispatcher, executor, types

bot = Bot('TOKEN')
dp = Dispatcher(bot)

async def on_start(_):
    print('Бот запущен')


@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer('Привет всем')


@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    await message.answer('Пока ничего не умею')

@dp.message_handler()
async def mes_all(message: types.Message):
    await message.answer('Ловлю всё')

executor.start_polling(dp, skip_updates=True, on_startup=on_start)    