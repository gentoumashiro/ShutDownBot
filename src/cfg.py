from aiogram import Bot, Dispatcher


TOKEN = ''  # you api token. get from @BotFather
ADMIN_ID = tuple()  # tuple of telegram user ids, can be obtained from @getmyid_bot


bot = Bot(TOKEN)
dp = Dispatcher(bot)
