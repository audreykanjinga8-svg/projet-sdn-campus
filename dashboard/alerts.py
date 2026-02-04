import asyncio
from telegram import Bot

TOKEN = "8284521150:AAGCFV3QZ3Ok90MLNzLai-F7_Jk9CDsFSG0"
CHAT_ID = 5249947478  # ton vrai chat ID (int)

bot = Bot(token=TOKEN)

def send_alert(message):
    """Envoie un message Telegram via ton bot (async)"""
    async def _send():
        await bot.send_message(chat_id=CHAT_ID, text=message)
    asyncio.run(_send())

