from aiogram.utils import executor #для запуска бота
import logging
from config import db


from handler import client,callback,admin,extra



extra.reg_hand_extra(db)
callback.reg_hand_callback(db)
client.rec_client(db)
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)
    