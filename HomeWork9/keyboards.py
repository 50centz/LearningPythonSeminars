from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_main_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

btn_help = KeyboardButton('/help')
btn_start = KeyboardButton('/start🏃')
btn_reset = KeyboardButton('/reset')
btn_total = KeyboardButton('/total')
btn_location = KeyboardButton('Геолакация', request_location=True)
btn_contact = KeyboardButton('Перезвонить мне ☎️', request_contact=True)

kb_main_menu.add(btn_start, btn_help, btn_reset, btn_total)
kb_main_menu.add(btn_location, btn_contact)

