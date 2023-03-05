from aiogram import Dispatcher, Bot
from  decouple import config
TOKEN=config('TOKEN')
# TOKEN=6191289864:AAERAn2n6dPvgH8536bLlRlABVFnkVLL5mA
ADMIN=(1970278827,1970278827)
bot = Bot(TOKEN)
db = Dispatcher(bot=bot)