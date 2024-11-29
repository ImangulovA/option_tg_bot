import logging

# Configure logging
logging.basicConfig(
    filename="bot/logs/bot_usage.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_usage(event: str, chat_id: int, username: str = "Unknown"):
    logging.info(f"Event: {event} | Chat ID: {chat_id} | Username: {username}")

def parse_poll_arguments(message_lines):
    options = []
    title = "Choose your options:"
    last_option = "nogotochki"
    allow_multiple_answers = True

    for line in message_lines:
        line = line.strip()
        if line.startswith("--title"):
            title = line[len("--title"):].strip()
        elif line.startswith("--last"):
            last_option = line[len("--last"):].strip()
        elif line.startswith("--type"):
            poll_type = line[len("--type"):].strip().lower()
            allow_multiple_answers = poll_type != "single"
        else:
            options.append(line)

    if last_option:
        options.append(last_option)

    return title, options, allow_multiple_answers
