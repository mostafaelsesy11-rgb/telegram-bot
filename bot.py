import os
import asyncio
import arabic_reshaper

from bidi.algorithm import get_display
from telegram import Bot

from moviepy import (
    VideoFileClip,
    AudioFileClip,
    TextClip,
    CompositeVideoClip
)

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

VERSE = "﴿ وَذَكِّرْ فَإِنَّ الذِّكْرَىٰ تَنفَعُ الْمُؤْمِنِينَ ﴾"

async def main():

    reshaped = arabic_reshaper.reshape(VERSE)
    arabic_text = get_display(reshaped)

    video = VideoFileClip("rain.mp4").subclipped(0, 15)

    audio = AudioFileClip("quran.mp3").subclipped(0, 15)

    txt = TextClip(
        text=arabic_text,
        font="Amiri-Regular.ttf",
        font_size=70,
        color="white",
        method="caption",
        size=(900, None)
    ).with_position(("center", "center")).with_duration(15)

    final = CompositeVideoClip([video, txt])

    final = final.with_audio(audio)

    final.write_videofile(
        "reel.mp4",
        fps=24,
        codec="libx264",
        audio_codec="aac"
    )

    with open("reel.mp4", "rb") as vid:
        await bot.send_video(
            chat_id=CHAT_ID,
            video=vid,
            caption="🤍 قرآن كريم"
        )

    print("✅ تم إرسال الريلز")

asyncio.run(main())