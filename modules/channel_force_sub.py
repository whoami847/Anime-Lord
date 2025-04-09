# File: AnimeLordBot/modules/channel_force_sub.py
from pyrogram import Client, filters
from pyrogram.types import Message
from config.config import Config

@Client.on_message(filters.private)
async def check_subscription(client, message: Message):
    if Config.FORCE_SUB:
        try:
            member = await client.get_chat_member(Config.FORCE_SUB, message.from_user.id)
            if member.status not in ["member", "administrator", "creator"]:
                raise Exception()
        except:
            await message.reply(
                f"দয়া করে আমাদের চ্যানেলে যোগ দিন: https://t.me/{Config.FORCE_SUB}"
            )
            return
