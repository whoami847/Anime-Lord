# File: AnimeLordBot/modules/font_style.py
from pyrogram import Client, filters
from pyrogram.types import Message

FONT_PREFIX = "Aɴɪᴍᴇ Lᴏʀᴅ"

@Client.on_message(filters.private & ~filters.command(["start", "help"]))
async def styled_message(client, message: Message):
    await message.reply(f"{FONT_PREFIX}:\n{message.text}")
