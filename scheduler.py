from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot
from config import API_TOKEN

bot = Bot(token=API_TOKEN)
scheduler = AsyncIOScheduler()

# Функция для отправки записей
async def send_note(user_id, note):
    await bot.send_photo(chat_id=user_id, photo=note['image'], caption=note['text'])

# Инициализация планировщика при запуске бота
async def on_startup(dp):
    scheduler.start()
