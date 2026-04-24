from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont
import numpy as np

W, H = 1080, 1920

# ✳️ الآية
import random

ayat = [
"فَإِنَّ مَعَ الْعُسْرِ يُسْرًا",
"وَبَشِّرِ الصَّابِرِينَ",
"إِنَّ اللَّهَ مَعَ الصَّابِرِينَ",
"أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ",
"وَقُل رَّبِّ زِدْنِي عِلْمًا",
"إِنَّ مَعِيَ رَبِّي سَيَهْدِينِ",
"لَا تَقْنَطُوا مِن رَّحْمَةِ اللَّهِ",
"وَاللَّهُ خَيْرُ الرَّازِقِينَ"
]

text = random.choice(ayat)

# 🟡 إنشاء صورة للنص بخلفية شفافة
img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

font = ImageFont.load_default()

bbox = draw.textbbox((0, 0), text, font=font)
text_w = bbox[2] - bbox[0]
text_h = bbox[3] - bbox[1]

pos = ((W - text_w)//2, (H - text_h)//2)

draw.text(pos, text, fill=(255, 255, 255, 255), font=font)

img_path = "text.png"
img.save(img_path)

# 🟢 خلفية احترافية متحركة (Gradient Motion)
def make_frame(t):
    base = np.zeros((H, W, 3), dtype=np.uint8)

    # تدرج لوني بسيط (أخضر/رمادي هادي)
    r = int(20 + 10 * np.sin(t))
    g = int(30 + 10 * np.sin(t))
    b = int(25 + 10 * np.cos(t))

    base[:] = (r, g, b)
    return base

bg = VideoClip(make_frame, duration=6)

# 🟢 النص
txt = ImageClip(img_path).set_duration(6)

# 🟢 دمج + حركة بسيطة
video = CompositeVideoClip([bg, txt])

video = video.fadein(1).fadeout(1)

# ✨ زووم خفيف (احترافي)


# 🟢 إخراج
video.write_videofile("reel_pro_plus.mp4", fps=24)