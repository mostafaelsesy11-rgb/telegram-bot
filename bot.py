import os
import asyncio
from telegram import Bot

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

async def main():
    print("✅ البوت بدأ")

    while True:
        try:
            await bot.send_message(chat_id=CHAT_ID, text="🔥 البوت شغال 100%")
            print("📩 تم إرسال رسالة")
        except Exception as e:
            print("❌ Error:", e)

        await asyncio.sleep(60)  # كل دقيقة

asyncio.run(main())