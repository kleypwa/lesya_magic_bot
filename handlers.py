# handlers.py
from aiogram import Bot, Dispatcher, types
from logging_config import setup_logging
from database import add_note, get_all_notes
from datetime import datetime

logger = setup_logging()

# Инициализация бота и диспетчера
def create_bot(api_token):
    bot = Bot(token=api_token)
    dp = Dispatcher(bot)
    return bot, dp

# Обработчик команды /start
async def send_welcome(message: types.Message):
    logger.info(f"User {message.from_user.id} started the bot.")
    await message.reply("Welcome! Use /add to add a new note.")

# Обработчик команды /add
async def add_note_handler(message: types.Message):
    logger.info(f"User {message.from_user.id} initiated adding a new note.")
    await message.reply("Send me the text of the note.")

    # Ожидаем текстовое сообщение
    text_message = await message.bot.wait_for("message")
    text = text_message.text
    await message.reply("Send me the image URL.")

    # Ожидаем ссылку на изображение
    image_message = await message.bot.wait_for("message")
    image_url = image_message.text

    await message.reply("Send me the time in format HH:MM.")

    # Ожидаем время
    time_message = await message.bot.wait_for("message")
    try:
        time_when_send = datetime.strptime(time_message.text, "%H:%M")
        add_note(text, image_url, time_when_send)
        await message.reply("Note successfully added!")
    except ValueError:
        await message.reply("Invalid time format. Please use HH:MM.")
        logger.warning(f"User {message.from_user.id} entered an invalid time format.")

# Обработчик команды /notes
async def list_notes_handler(message: types.Message):
    logger.info(f"User {message.from_user.id} requested all notes.")
    notes = get_all_notes()
    if notes:
        for note in notes:
            await message.reply(f"Text: {note['text']}\nImage: {note['image_url']}\nTime: {note['timeWhenSend']}")
    else:
        await message.reply("No notes found.")
