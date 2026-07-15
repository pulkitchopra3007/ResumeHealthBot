"""
File Manager

Responsible for handling resume files.
"""

from pathlib import Path


class FileManager:
    """Handles file storage operations."""

    def __init__(self):
        self.upload_folder = Path("assets/uploads")
        self.upload_folder.mkdir(parents=True, exist_ok=True)

    def get_upload_folder(self):
        """Return upload folder path."""
        return self.upload_folder