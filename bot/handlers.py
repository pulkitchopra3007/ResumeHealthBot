"""
Bot Handlers
"""

from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command."""

    await update.message.reply_text(
        "🤖 Welcome to Resume Health Bot!\n\n"
        "📄 Send me your resume in PDF format to begin analysis."
    )