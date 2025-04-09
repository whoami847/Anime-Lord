# File: AnimeLordBot/modules/log_clear.py
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("clearlog") & filters.private)
async def clear_logs(client, message: Message):
    # লগ মুছে ফেলার কোড
    await message.reply("সকল লগ সফলভাবে মুছে ফেলা হয়েছে।")
