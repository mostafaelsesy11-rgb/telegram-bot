import os
import asyncio
from telegram import Bot
from PIL import Image, ImageDraw, ImageFont

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

async def main():

    img = Image.new("RGB", (1080, 1920), color=(10, 10, 10))

    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("Amiri-Regular.ttf", 70)

    text = "﴿ وَذَكِّرْ فَإِنَّ الذِّكْرَىٰ تَنفَعُ الْمُؤْمِنِينَ ﴾"

    draw.text((100, 900), text, font=font, fill="white")

    img.save("quran.png")

    with open("quran.png", "rb") as photo:
        await bot.send_photo(chat_id=CHAT_ID, photo=photo)

    print("✅ تم إرسال الصورة")

asyncio.run(main())