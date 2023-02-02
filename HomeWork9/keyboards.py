from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_main_menu1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_main_menu2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

btn_help = KeyboardButton('/help')
btn_start = KeyboardButton('/start🏃')
btn_reset = KeyboardButton('/reset')
btn_total = KeyboardButton('/total')
btn_location = KeyboardButton('Геолакация', request_location=True)
btn_contact = KeyboardButton('Перезвонить мне ☎️', request_contact=True)
btn_change = KeyboardButton('/change')

kb_main_menu1.add(btn_change, btn_start, btn_reset)
kb_main_menu2.add(btn_change)
kb_main_menu2.add(btn_location, btn_contact)
