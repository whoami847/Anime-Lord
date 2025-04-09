# File: AnimeLordBot/modules/user_activity.py
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.private)
async def track_activity(client, message: Message):
    user_id = message.from_user.id
    # এখানে ইউজারের অ্যাক্টিভিটি লগ ডাটাবেজে সংরক্ষণ করা হবে
