from aiogram import executor
from cfg import bot, dp, ADMIN_ID
from handlers import logic, echo


logic.register_handlers_client(dp)
echo.register_handlers_client(dp)


async def on_startup(_):
    print(f"[+] Bot is launched")
    await bot.send_message(ADMIN_ID[0], f"[+] Bot is launched")


async def on_shutdown(_):
    print(f"[-] Bot is done")
    await bot.send_message(ADMIN_ID[0], f"[-] Bot is done")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)