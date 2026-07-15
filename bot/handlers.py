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
async def receive_resume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Receive resume PDF."""

    document = update.message.document

    if document is None:
        return

    if not document.file_name.lower().endswith(".pdf"):
        await update.message.reply_text(
            "❌ Please upload your resume in PDF format only."
        )
        return

    await update.message.reply_text(
        f"✅ Resume received!\n\nFilename: {document.file_name}"
    )