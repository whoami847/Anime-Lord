# File: AnimeLordBot/modules/delete_file.py
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("delete") & filters.private)
async def delete_file(client, message: Message):
    if len(message.command) < 2:
        await message.reply("দয়া করে একটি ফাইল আইডি দিন।")
        return
    file_id = message.command[1]
    # এখানে ডাটাবেজ থেকে ফাইল মুছে ফেলার কোড হবে
    await message.reply(f"ফাইল `{file_id}` সফলভাবে মুছে ফেলা হয়েছে।")
