# File: AnimeLordBot/main.py

from pyrogram import Client
import os
from dotenv import load_dotenv
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

# Load environment variables
load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Initialize bot client
app = Client(
    "AnimeLordBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "modules"}
)

# Health check HTTP server for Koyeb
class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running.")

def run_server():
    server = HTTPServer(('0.0.0.0', 8080), HealthHandler)
    server.serve_forever()

# Start the fake HTTP server in a background thread
threading.Thread(target=run_server, daemon=True).start()

# Run the bot
if __name__ == "__main__":
    print("Bot is starting...")
    app.run()
