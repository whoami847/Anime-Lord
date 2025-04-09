# File: AnimeLordBot/modules/custom_buttons.py
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.command("button") & filters.private)
async def custom_button(client, message: Message):
    button = [[InlineKeyboardButton("Visit", url="https://example.com")]]
    await message.reply("এই বাটন ব্যবহার করুন:", reply_markup=InlineKeyboardMarkup(button))
