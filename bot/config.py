import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Bot token
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise ValueError("Bot token not found. Please set TELEGRAM_BOT_TOKEN in your environment or .env file.")