"""
Resume Parser
"""

import re


class ResumeParser:

    def __init__(self, text):
        self.text = text

    def get_email(self):
        pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
        match = re.search(pattern, self.text)

        if match:
            return match.group()

        return None