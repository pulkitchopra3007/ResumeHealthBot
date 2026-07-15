"""
Resume Parser
"""

from parsers.extractors import (
    EmailExtractor,
    PhoneExtractor,
    SkillExtractor,
)


class ResumeParser:

    def __init__(self, text):
        self.text = text

    def parse(self):

        return {
            "name": None,
            "email": EmailExtractor.extract(self.text),
            "phone": PhoneExtractor.extract(self.text),
            "skills": SkillExtractor.extract(self.text),
            "education": [],
            "experience": [],
            "projects": [],
            "certifications": [],
            "links": [],
        }