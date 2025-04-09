# File: AnimeLordBot/modules/auto_post.py
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("autopost") & filters.private)
async def auto_post_handler(client, message: Message):
    if len(message.command) < 2:
        await message.reply("দয়া করে একটি চ্যানেল ইউজারনেম দিন।")
        return
    channel = message.command[1]
    await message.reply(f"আপনার ফাইল এখন থেকে {channel} চ্যানেলে অটো-পোস্ট হবে।")
    # এখানে অটোপোস্ট সেটআপ সংরক্ষণের কোড হবে
