# File: AnimeLordBot/modules/custom_sub_message.py
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("submessage") & filters.private)
async def set_sub_message(client, message: Message):
    await message.reply("সাবস্ক্রিপশন মেসেজ কাস্টমাইজ করার ফিচার কাজ করছে।")
