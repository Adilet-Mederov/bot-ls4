from aiogram import Bot, Dispatcher, executor, types
import logging
from config import db
from handler import client,callback,admin,extra



client.rec_client(db)
callback.reg_hand_callback(db)
admin.reg_ban(db)
extra.reg_hand_extra(db)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)
    