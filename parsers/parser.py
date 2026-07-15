"""
Resume Parser
"""

from parsers.extractors import (
    EmailExtractor,
    PhoneExtractor,
)


class ResumeParser:

    def __init__(self, text: str):
        self.text = text

    def parse(self):

        return {
            "email": EmailExtractor.extract(self.text),
            "phone": PhoneExtractor.extract(self.text),
        }