from aiogram import types,Dispatcher
from config import bot,db
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


async def quiz2(massage:types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton('next', callback_data='button')
    markup.add(button)

    ques = 'Кем они являются друг другу?'
    answer = [
        'Братьями!',
        'Друзьями!',
        'Коллегами!',
        'Сестрами!',
        'Не знаю!'
    ]
    photo = open('media/cba.jpg', 'rb')
    await bot.send_photo(massage.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=massage.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=12,
    )
def reg_hand_callback(db:Dispatcher):
    db.register_callback_query_handler(quiz2, text='button')
    