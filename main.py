# File: AnimeLordBot/main.py
from config.config import Config
from modules import register_handlers

from pyrogram import Client, idle

bot = Client(
    "AnimeLordBot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

register_handlers(bot)

print("Bot is running...")

bot.start()
idle()
bot.stop()
