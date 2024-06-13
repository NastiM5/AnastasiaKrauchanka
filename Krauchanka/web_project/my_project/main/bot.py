# import time
# import logging
# from aiogram import Bot, Dispatcher, types

# TOKEN='7193958987:AAGT32MyPYRx7fFWcZrm9NLPcm7WIPGGd-0'
# bot=Bot(token=TOKEN)
# dp=Dispatcher(bot=bot)
# @dp.message_handler(commands=['start'])
# async def start_handler (message: types.Message):
#     user_id=message.from_user.id #(message.chat.id, 'Привет')
#     user_full_name=message.from_user.full_name
#     logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')

#     await message.reply("привет")
