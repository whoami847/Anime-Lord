# File: AnimeLordBot/modules/auto_post_config.py
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("autoconfig") & filters.private)
async def auto_post_config(client, message: Message):
    await message.reply("অটো-পোস্ট কনফিগারেশন সফলভাবে আপডেট হয়েছে।")
