# File: AnimeLordBot/config/config.py
import os

class Config:
    API_ID = int(os.environ.get("API_ID", "28774737"))
    API_HASH = os.environ.get("API_HASH", "851190ab85bb0b6dd547fff8e3c35b73")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7352104242:AAEpIiqsTduGBYON09wYdK-T9JLXBw7JdJE")
    OWNER_ID = int(os.environ.get("OWNER_ID", "7282066033"))
    FORCE_SUB = os.environ.get("FORCE_SUB", None)
