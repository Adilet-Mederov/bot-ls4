from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor #для запуска бота
import logging
import decouple
from decouple import config
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


TOKEN=config('TOKEN')

bot = Bot(TOKEN)
db = Dispatcher(bot=bot)

@db.message_handler(commands=['start' , 'hello'])
async def start_handler(massage:types.message):
    await massage.answer('Hello!')
    await bot.send_message(massage.from_user.id,f'{massage.from_user.first_name}\n'
                                                f'Для активации викторины---> /quiz')

    # await massage.answer('Пока что всё!')


# опросник\викторина
@db.message_handler(commands=['quiz'])
async def quiz1(massage: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton('next', callback_data='button')
    markup.add(button)
    ques = 'Название Мультфильма?'
    answer = [
        'Маша и Медведь!',
        'Молния Маквин ',
        'Губка Боб квадратные штаны!',
        'Скуби-Ду!',
        'Не знаю!'
    ]
    photo = open(media/) 

    await bot.send_poll(
        chat_id=massage.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Правильно!',
        open_period=10,
        reply_markup=markup
    )


@db.callback_query_handler(text='button')
async def quiz2(call:types.CallbackQuery):
    ques = 'Как зовут этого персонажа?'
    answer = [
        'Мэтр',
        'Губка боб',
        'Патрик',
        'Маша',
        'Не знаю!'
    ]
    # photo = open('')
    # await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='Првильно!',
        open_period=10,

    )


@db.message_handler()
async def echo(massage: types.Message):
    await bot.send_message(massage.from_user.id, massage.text)
    await massage.answer('Что-то еще?')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)