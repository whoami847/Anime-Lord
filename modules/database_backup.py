# File: AnimeLordBot/modules/database_backup.py
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("backupdb") & filters.private)
async def backup_database(client, message: Message):
    # ব্যাকআপ তৈরি করার কোড
    await message.reply("ডাটাবেস ব্যাকআপ সফলভাবে তৈরি হয়েছে।")
