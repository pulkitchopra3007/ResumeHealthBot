"""
Resume Health Bot Configuration
--------------------------------
This file stores project-wide configuration values.

Author: Resume Health Team
Version: 1.0.0
"""

# =========================
# BOT CONFIGURATION
# =========================

BOT_NAME = "Resume Health"
BOT_VERSION = "1.0.0"

# Development Token
# NOTE:
# Replace with a new token before production.
BOT_TOKEN = "PASTE_YOUR_TOKEN_HERE"

# =========================
# SUPPORTED FILES
# =========================

SUPPORTED_FILE_TYPES = (
    ".pdf",
    ".docx",
)

# =========================
# FILE LIMITS
# =========================

MAX_FILE_SIZE_MB = 10

# =========================
# DEFAULT SETTINGS
# =========================

DEFAULT_SCORE = 100