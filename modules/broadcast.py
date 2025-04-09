# File: AnimeLordBot/modules/broadcast.py
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("broadcast") & filters.private)
async def broadcast_message(client, message: Message):
    if len(message.command) < 2:
        await message.reply("দয়া করে একটি মেসেজ দিন।")
        return
    broadcast_text = message.text.split(None, 1)[1]
    # সকল ইউজারে মেসেজ পাঠানোর কোড এখানে হবে
    await message.reply("ব্রডকাস্ট মেসেজ পাঠানো শুরু হয়েছে।")
