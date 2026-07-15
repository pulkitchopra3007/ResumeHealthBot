"""
Resume Health Bot Configuration

This file stores all project settings.
"""

# Telegram Bot Token
BOT_TOKEN = ""

# Bot Information
BOT_NAME = "Resume Health Bot"
BOT_VERSION = "1.0.0"

# Supported File Types
SUPPORTED_FILES = [
    ".pdf",
    ".docx"
]

# Maximum Resume Size (10 MB)
MAX_FILE_SIZE = 10 * 1024 * 1024

# Default Resume Score
DEFAULT_SCORE = 100