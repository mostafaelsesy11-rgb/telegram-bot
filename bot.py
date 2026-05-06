from telegram import Bot
import asyncio

TOKEN = "8791016523:AAFgWjFc1Ob9HNCtb_zopTN3JyrWnvVWjbU"
CHAT_ID = 6063339002

bot = Bot(token=TOKEN)

async def main():
    await bot.send_message(chat_id=CHAT_ID, text="🔥 شغال")

asyncio.run(main())