# app.py
from aiogram import executor
from config import API_TOKEN
from handlers import create_bot, send_welcome, add_note_handler, list_notes_handler
from logging_config import setup_logging

logger = setup_logging()

# Создание бота и диспетчера
bot, dp = create_bot(API_TOKEN)

# Регистрация обработчиков
dp.register_message_handler(send_welcome, commands=['start'])
dp.register_message_handler(add_note_handler, commands=['add'])
dp.register_message_handler(list_notes_handler, commands=['notes'])

if __name__ == '__main__':
    logger.info("Bot started.")
    executor.start_polling(dp, skip_updates=True)
