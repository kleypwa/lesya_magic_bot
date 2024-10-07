# database.py
from pymongo import MongoClient
from config import MONGO_URI
from logging_config import setup_logging

logger = setup_logging()

# Подключение к MongoDB
client = MongoClient(MONGO_URI)
db = client['bot_database']
notes_collection = db['notes']

# Функция для добавления новой записи
def add_note(text, image_url, time_when_send):
    try:
        note = {
            "text": text,
            "image_url": image_url,
            "timeWhenSend": time_when_send
        }
        notes_collection.insert_one(note)
        logger.info("Note added to database.")
    except Exception as e:
        logger.error(f"Error adding note: {e}")

# Функция для получения всех записей
def get_all_notes():
    try:
        notes = notes_collection.find()
        logger.info("Retrieved all notes from database.")
        return notes
    except Exception as e:
        logger.error(f"Error retrieving notes: {e}")
        return []
