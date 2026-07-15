"""
Bot Handlers
"""

from telegram import Update
from telegram.ext import ContextTypes

from utils.file_manager import save_resume
from utils.pdf_parser import extract_text
from parsers.parser import ResumeParser


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

    # Save Resume
    file_path = await save_resume(document)

    # Extract Text
    text = extract_text(file_path)

    # Parse Resume
    parser = ResumeParser(text)
    resume = parser.parse()

    # Reply
    await update.message.reply_text(
        f"""✅ Resume Parsed

👤 Name:
{resume.name}

📧 Email:
{resume.email}

📞 Phone:
{resume.phone}

🛠 Skills:
{", ".join(resume.skills) if resume.skills else "Not Found"}

🎓 Education:
{", ".join(resume.education) if resume.education else "Not Found"}

💼 Experience:
{", ".join(resume.experience) if resume.experience else "Not Found"}
"""
    )