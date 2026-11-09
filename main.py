import asyncio
import random
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import pytz

# Твои данные
BOT_TOKEN = "9173903696:AAFQ0iZkzeATs0eiPeFVnHzW_WKQ6lPWuS4"
ZLATA_CHAT_ID = 5089212421  # Chat ID

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
scheduler = AsyncIOScheduler()

# Пожелания для Златы
WISHEES = [
    "Доброе утро, Злата! ✨ Пусть этот день принесёт тебе много улыбок, тепла и радости!",
    "Прекрасного утра, любимая! ☀️ Желаю тебе невероятно уютного и успешного дня!",
    "С добрым утром, Злата! 🌸 Пусть всё задуманное сегодня сбывается легко и непринуждённо.",
    "Доброе утро! 💕 Пусть твоя улыбка озаряет этот день так же ярко, как солнце!",
    "Утречка, Злата! ☕ Начни этот день с отличного настроения, а я всегда буду рядом."
]

# Ссылки на картинки
IMAGES = [
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
    "https://images.unsplash.com/photo-1499750310107-5fef28a66643",
    "https://images.unsplash.com/photo-1518495973542-4542c06a5843",
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb"
]

async def send_morning_card():
    wish = random.choice(WISHEES)
    image_url = random.choice(IMAGES)
    try:
        await bot.send_photo(
            chat_id=ZLATA_CHAT_ID,
            photo=image_url,
            caption=wish
        )
        print("Утренняя открытка успешно отправлена!")
    except Exception as e:
        print(f"Ошибка при отправке: {e}")

async def main():
    tz = pytz.timezone("Europe/Moscow")
    
    # Отправка каждый день в 08:00 утра
    scheduler.add_job(
        send_morning_card, 
        trigger="cron", 
        hour=8, 
        minute=0, 
        timezone=tz
    )
    
    scheduler.start()
    print("Бот запущен и следит за расписанием...")
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
