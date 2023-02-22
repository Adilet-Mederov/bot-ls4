from aiogram import Dispatcher, Bot
from  decouple import config
TOKEN=config('TOKEN')
# TOKEN=6191289864:AAERAn2n6dPvgH8536bLlRlABVFnkVLL5mA

bot = Bot(TOKEN)
db = Dispatcher(bot=bot)