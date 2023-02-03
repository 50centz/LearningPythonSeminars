from create import dp, types
from random import randint
from keyboards import kb_main_menu
from datetime import datetime

total = 0
candy = 0


@dp.message_handler(commands=['start']) 
async def mes_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name} ! Ты на конфетном поле боя !', reply_markup=kb_main_menu)
    # await message.answer(f'Hello, {message.from_user.first_name}\nМеня зовут ТЕРМИНАТОР - 3\nЯ умею играть в конфеты')
    # await message.answer('Правила игры:\nТот, кто забирает последнюю конфету, выигрывает партию и забирает себе все  конфеты')
    # await message.answer('Количество конфет можно задать командой:\n/set "Количество конфет"')
    # await message.answer('Какое количество конфет можно взять за один ход, командой:\n/candy "Конфет за один ход "')
    # await message.answer('Пример:\n/set 100\n/candy 7')

@dp.message_handler(commands=['help']) 
async def mes_help(message: types.Message):
    await message.answer('Бог поможет')

    user = []
    user.append(datetime.now())
    user.append(message.from_user.full_name)
    user.append(message.from_user.id)
    user.append(message.from_user.username)
    user = list(map(str, user))
    with open('log.txt', 'a', encoding='UTF-8') as data:
        data.write(':'.join(user) + '\n')



@dp.message_handler(content_types='location') 
async def mes_loc(message: types.Message):
    print(message)

@dp.message_handler(content_types='contact') 
async def mes_con(message: types.Message):
    print(message.contact.phone_number, message.contact.first_name, message.contact.last_name)
    await message.send_copy(1358277301)

    # print(message.answer_contact)

@dp.message_handler(commands=['set']) 
async def mes_set(message: types.Message):
    global total
    if len(message.text) < 6:
        await message.answer('Введите число\nПример: /set 100')
    elif len(message.text) > 5:
        a = message.text.split()[1].isdigit()
        if a == True:
            total = int(message.text.split()[1])
        else:
            await message.answer('Введите число\nПример: /set 100')
    await message.answer(f'Максимальное количество конфет установлено - {total}')                       

@dp.message_handler(commands=['candy']) 
async def mes_candy(message: types.Message):
    global candy
    if len(message.text) < 8:
        await message.answer('Введите число\nПример: /candy 7')   
    elif len(message.text) > 7:
        a = message.text.split()[1].isdigit()
        if a == True:
            candy = int(message.text.split()[1])
        else:
            await message.answer('Введите число\nПример: /candy 7')
        await message.answer(f'Максимально количество за одн ход установлено {candy}')    


@dp.message_handler(commands=['reset']) 
async def mes_reset(message: types.Message):
    global total
    global candy 
    total = 0
    candy = 0 

@dp.message_handler(commands=['total']) 
async def mes_total(message: types.Message):
    global total
    global candy
    if total <= 0:
        await message.answer(f'Количество конфет = {total}\nВведите количество конфет командой /set')
    elif total > 0:    
        await message.answer(f'Осталось конфет - {total}') 
     
@dp.message_handler() 
async def mes_all(message: types.Message):
    global total
    global candy

    if message.text.isdigit():
        if int(candy) == 0:
            await message.answer('Введите количество конфет командой /candy')
            return
        if int(message.text) > candy:
            await message.answer(f'цифра должна быть меньше либо равно {candy}')
            return 
        else:
            total -= int(message.text)
            if total <= 0:
                await message.answer(f'Выиграл {message.from_user.first_name} !!!!!')
                return
        await message.answer(f'Осталось {total} конфет\nТеперь ходит ТЕРМИНАТОР - 3')
        b = randint(1, candy)
        total -= b
        await message.answer(f'ТЕРМИНАТОР - 3 взял {b} конфет(ы)\nОсталось {total} конфет')
        if total <= 0:
            await message.answer(f'Выиграл ТЕРМИНАТОР - 3 !!!!!')
            return
    else:
        await message.answer('ТЕРМИНАТОР - 3:\nЯ умею работать только с цифрами, я только учусь !!!!')
           
      






