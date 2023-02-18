# from aiogram import Bot, Dispatcher, types
# # from aiogram.utils import executor #для запуска бота
# # import logging
# # import decouple
# # from decouple import config
# # from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
# #
# #
# # TOKEN=config('TOKEN')
# #
# # bot = Bot(TOKEN)
# # db = Dispatcher(bot=bot)
# #
# # @db.message_handler(commands=['start' , 'hello'])
# # async def start_handler(massage:types.message):
# #     await massage.answer('HELLO!')
# #     await bot.send_message(massage.from_user.id,f'{massage.from_user.first_name}')
# #     await massage.answer('Пока что всё!')
# #
# # #Опросник\Викторина
# # @db.message_handler(commands=['quiz'])
# # async def quiz1(massage:types.Message):
# #     markup=InlineKeyboardMarkup()
# #     button=InlineKeyboardButton('Next',callback_data='button')
# #     ques = 'Название мультфильма?'
# #     answer =[
# #         'Маша и Медведь!',
# #         'Скуби-Ду!',
# #         'Губка боб квадратные штаны!',
# #         'Не знаю!'
# #     ]
# #     photo=open('media/cba.jpg', 'rd')
# #     await bot.send_photo(call.from_user.id,photo=photo)
# #
# #
# #
# #     await bot.send_poll(
# #         chat_id=massage.from_user.id,
# #         question=ques,
# #         options=answer,
# #         is_anonymous=False,
# #         type='quiz',
# #         correct_option_id=3,
# #         open_period=2*5
# #     )
# #
# # @db.callback_query_handler(text='button')
# # async def quiz2(call:types.CallbackQuery):
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # @db.message_handler()
# # async def echo(massege:types.Message):
# #     await bot.send_message(massege.from_user.id,massege.text)
# #
# #
# # if __name__ == '__main__':
# #     logging.basicConfig(level=logging.INFO)
# #     executor.start_polling(db, skip_updates=True)