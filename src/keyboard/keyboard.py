from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


shutdown_button = KeyboardButton('Shutdown my computer')
help_button = KeyboardButton("Help")

kb_client = ReplyKeyboardMarkup(resize_keyboard=True).add(help_button)
kb_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(shutdown_button).add(help_button)
