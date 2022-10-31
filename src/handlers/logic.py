import sys
import os

from time import localtime, strftime, sleep
from aiogram import Dispatcher, types
from cfg import bot, ADMIN_ID
from keyboard import kb_admin, kb_client


OPERATION_SYSTEM = sys.platform.lower().strip()


async def is_admin(user_id: int) -> bool:
    if not (user_id in ADMIN_ID):
        await bot.send_message(user_id, f"Sorry. but you are not in admin list\n"
                                        f"You cannot use this bot😔", reply_markup=kb_client)
        await bot.send_message(ADMIN_ID[0], f"{user_id} is trying to use your bot\n"
                                            f"at: {strftime('%d/%m/%Y, %H:%M:%S', localtime())}")
        return False
    return True


async def start(message: types.message) -> None:
    user_id = message.from_user.id
    if await is_admin(user_id):
        await bot.send_message(user_id, f"Halo my admin,\n{message.from_user.first_name}!", reply_markup=kb_admin)
        return None
    await bot.send_message(user_id, f"Press 'help' button to view more information!", reply_markup=kb_client)


async def reply_to_help(message: types.message) -> None:
    user_id = message.from_user.id
    await bot.send_message(user_id, f"This bot is using to shutdown a local pc via telegram, if you cannot use this "
                                    f"bot: \n"
                                    f"1) you can copy my git repo below and start this script on your local machine \n"
                                    f"2) you can add another telegram account id at: \n./cfg in ADMIN_ID list"
                                    f" \n\n----------------------------------------------\n"
                                    f"GIT: https://github.com/gentoumashiro/ShutDownPC_bot\n----------------------------------------------")


async def power_off_pc(message: types.message) -> None:
    user_id = message.from_user.id

    if await is_admin(user_id):
        for i in range(3, 0, -1):
            await bot.send_message(user_id, f"[{i}] Shutting down your pc...", reply_markup=kb_admin)
            sleep(1)

        match OPERATION_SYSTEM:
            case 'linux':
                os.system("shutdown -h now")
            case 'win32':
                os.system("shutdown /p")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, lambda message: message.text.lower().strip() in ('start', '/start'))
    dp.register_message_handler(reply_to_help, lambda message: message.text.lower().strip() in ("help", "/help"))
    dp.register_message_handler(power_off_pc, lambda message: message.text.lower().strip() in (
        "shutdown my computer", "/shutdown my computer"))
