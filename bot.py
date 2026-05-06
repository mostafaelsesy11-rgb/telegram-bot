import os
import asyncio
from telegram import Bot
from datetime import datetime

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

TARGET_HOUR = 12  # الساعة 12
TARGET_MINUTE = 0

async def main():
    print("✅ البوت شغال")

    while True:
        now = datetime.now()

        if now.hour == TARGET_HOUR and now.minute == TARGET_MINUTE:
            try:
                await bot.send_message(chat_id=CHAT_ID, text="🔥 الرسالة اليومية")
                print("📩 تم الإرسال")
                await asyncio.sleep(60)  # يمنع التكرار
            except Exception as e:
                print("❌ Error:", e)

        await asyncio.sleep(30)

asyncio.run(main())