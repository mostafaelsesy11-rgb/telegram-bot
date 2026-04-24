import asyncio
import datetime
import os
from telegram import Bot

TOKEN = "8623245671:AAGwJlyDJTQMh_irr2nKKXfhTlSsHRucV0E"
CHAT_ID = "6063339002"
VIDEO = "reel_pro_plus.mp4"

bot = Bot(token=TOKEN)

async def send_video():
    await bot.send_video(
        chat_id=CHAT_ID,
        video=open(VIDEO, "rb"),
        caption="📖 آية قرآنية يومية"
    )

def seconds_until(hour, minute):
    now = datetime.datetime.now()
    target = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

    if target <= now:
        target += datetime.timedelta(days=1)

    return (target - now).total_seconds()

async def job():
    while True:
        wait_time = seconds_until(14, 20) # 
        print(f"⏳ انتظار {int(wait_time)} ثانية لميعاد الإرسال...")
        await asyncio.sleep(wait_time)

        print("🎬 تجهيز الفيديو...")
        os.system("py pro_video.py")

        print("📤 إرسال الفيديو...")
        await send_video()

        print("✅ تم الإرسال اليومي بنجاح")

asyncio.run(job())