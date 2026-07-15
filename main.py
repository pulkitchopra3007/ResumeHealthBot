"""
Resume Health Bot
Main Entry Point
"""

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

from config import BOT_NAME, BOT_VERSION, BOT_TOKEN


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start Command"""

    await update.message.reply_text(
        f"🤖 {BOT_NAME}\n\n"
        f"Version: {BOT_VERSION}\n\n"
        "✅ Bot Started Successfully.\n"
        "Welcome to Resume Health!"
    )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print(f"{BOT_NAME} v{BOT_VERSION} Started")

    app.run_polling()


if __name__ == "__main__":
    main()