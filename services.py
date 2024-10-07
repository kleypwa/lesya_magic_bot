from datetime import datetime, timedelta
from database import add_note, get_notes_by_user

async def create_note(user_id, text, image, time_str):
    try:
        send_time = datetime.strptime(time_str, "%H:%M").time()
        now = datetime.now()
        send_datetime = datetime.combine(now, send_time)
        
        if send_datetime < now:
            send_datetime += timedelta(days=1)
        
        note = {
            'user_id': user_id,
            'text': text,
            'image': image,
            'timeWhenSend': send_datetime
        }
        await add_note(note)
        return note, send_datetime

    except ValueError:
        raise ValueError("Некорректный формат времени")

async def get_user_notes(user_id):
    return await get_notes_by_user(user_id)
