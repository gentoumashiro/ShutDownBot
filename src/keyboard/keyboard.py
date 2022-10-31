from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


shutdown_button = KeyboardButton('Shutdown my computer')
sleep_button = KeyboardButton("Sleep")
help_button = KeyboardButton("Help")

kb_client = ReplyKeyboardMarkup(resize_keyboard=True).add(help_button)
kb_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(shutdown_button).add(sleep_button).add(help_button)
