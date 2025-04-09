# File: AnimeLordBot/modules/user_list.py
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("users") & filters.private)
async def get_users(client, message: Message):
    # ইউজার তালিকা দেখানোর জন্য ডাটাবেজ কল
    await message.reply("ইউজার লিস্ট:\n1. UserA\n2. UserB")
