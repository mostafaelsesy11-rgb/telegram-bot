import os
import asyncio
from telegram import Bot

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

async def main():
    print("✅ شغال")

    while True:
        try:
            with open("video.mp4", "rb") as vid:
                await bot.send_video(chat_id=CHAT_ID, video=vid, caption="🤍 قرآن كريم")

            print("📹 تم إرسال فيديو")

        except Exception as e:
            print("❌ Error:", e)

        await asyncio.sleep(86400)  # كل يوم

asyncio.run(main())