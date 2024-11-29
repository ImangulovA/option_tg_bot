from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from bot.utils import parse_poll_arguments, log_usage

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hi! Use /poll to create polls with optional arguments. Example:\n"
        "/poll\nOption 1\nOption 2\n--title Custom Poll\n--last Custom Last Option\n--type single"
    )
    log_usage("Start command triggered", update.effective_chat.id, update.effective_user.username)

async def poll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    username = update.effective_user.username or "Unknown"
    message_lines = update.message.text.split("\n")[1:]  # Skip the /poll line

    if len(message_lines) < 1:
        await update.message.reply_text("Usage:\n/poll\nOption 1\nOption 2\n--title Custom Poll\n--last Custom Last Option\n--type single")
        log_usage("Invalid poll command usage", chat_id, username)
        return

    title, options, allow_multiple_answers = parse_poll_arguments(message_lines)
    if len(options) < 2:
        await update.message.reply_text("A poll requires at least 2 options.")
        log_usage("Attempted to create a poll with insufficient options", chat_id, username)
        return

    await context.bot.send_poll(
        chat_id=chat_id,
        question=title,
        options=options,
        is_anonymous=False,
        allows_multiple_answers=allow_multiple_answers,
    )
    log_usage("Poll created successfully", chat_id, username)

# Export handlers for main.py
start = CommandHandler("start", start)
poll = CommandHandler("poll", poll)
