# File: AnimeLordBot/modules/activity_log.py
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("log") & filters.private)
async def show_log(client, message: Message):
    # লগ দেখানোর কোড
    await message.reply("এখানে আপনার অ্যাক্টিভিটি লগ।")
