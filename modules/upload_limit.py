# File: AnimeLordBot/modules/upload_limit.py
from pyrogram import Client, filters
from pyrogram.types import Message

UPLOAD_LIMIT_MB = 1024  # 1GB

@Client.on_message(filters.private & filters.document)
async def check_upload_size(client, message: Message):
    if message.document.file_size > UPLOAD_LIMIT_MB * 1024 * 1024:
        await message.reply("আপনার ফাইল সাইজ সীমা অতিক্রম করেছে (১GB)।")
        return
    await message.reply("ফাইল সফলভাবে গৃহীত হয়েছে!")
