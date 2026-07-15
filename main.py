"""
Resume Health Bot

Main Entry Point
"""

from telegram.ext import (
    Application,
    CommandHandler,
)

from config import BOT_NAME, BOT_VERSION, BOT_TOKEN
from bot.handlers import start


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print(f"{BOT_NAME} v{BOT_VERSION} Started Successfully")

    app.run_polling()


if __name__ == "__main__":
    main()