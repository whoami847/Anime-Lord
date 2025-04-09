# File: AnimeLordBot/config/config.py
import os

class Config:
    API_ID = int(os.environ.get("API_ID", "123456"))
    API_HASH = os.environ.get("API_HASH", "your_api_hash")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_bot_token")
    OWNER_ID = int(os.environ.get("OWNER_ID", "12345678"))
    FORCE_SUB = os.environ.get("FORCE_SUB", None)
