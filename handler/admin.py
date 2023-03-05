from aiogram import Dispatcher, types
from config import bot
from .extra import users



async def ban(message: types.Message):
    if message.chat.type != 'private':
        message_words = message.text.split()
        username = message_words[1]
        await bot.kick_chat_member(message.chat.id, user_id=users[f'{username}'])
        await message.answer('Он вышел сам!')
    else:
        await message.answer('это группа!')


def reg_ban(db: Dispatcher):
    db.register_message_handler(ban, commands=['ban'], commands_prefix=['!'])













