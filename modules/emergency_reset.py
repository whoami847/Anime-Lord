# File: AnimeLordBot/modules/emergency_reset.py
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("resetbot") & filters.private)
async def reset_bot(client, message: Message):
    await message.reply("বট রিসেট শুরু হয়েছে...")
    # রিসেট করার কোড
