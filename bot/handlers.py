"""
Bot Handlers
"""

from telegram import Update
from telegram.ext import ContextTypes

from utils.file_manager import save_resume
from utils.pdf_parser import extract_text


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

    # Save PDF
    file_path = await save_resume(document)

    # Extract text from PDF
    text = extract_text(file_path)

    # Print extracted text in Termux
    print("\n===== EXTRACTED TEXT =====\n")
    print(text)
    print("\n==========================\n")

    await update.message.reply_text(
        f"✅ Resume received!\n\n"
        f"Saved to:\n{file_path}"
    )