from telegram.ext import Application
from bot.config import TOKEN
from bot.handlers import start, poll

def main():
    application = Application.builder().token(TOKEN).build()

    # Add handlers
    application.add_handler(start)
    application.add_handler(poll)

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()