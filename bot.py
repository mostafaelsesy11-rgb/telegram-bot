import os
import asyncio
from telegram import Bot
from PIL import Image, ImageDraw

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

async def main():

    img = Image.new("RGB", (1080, 1920), color=(15, 15, 15))

    draw = ImageDraw.Draw(img)

    text = "﴿ وَذَكِّرْ فَإِنَّ الذِّكْرَىٰ تَنفَعُ الْمُؤْمِنِينَ ﴾"

    draw.text((120, 900), text, fill="white")

    img.save("quran.png")

    with open("quran.png", "rb") as photo:
        await bot.send_photo(chat_id=CHAT_ID, photo=photo)

    print("✅ تم إرسال الصورة")

asyncio.run(main())