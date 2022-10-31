from aiogram import Dispatcher, types


async def echo(message: types.Message):
    await message.delete()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(echo)
