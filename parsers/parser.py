"""
Resume Parser
"""

from core.resume import Resume

from parsers.extractors import (
    NameExtractor,
    EmailExtractor,
    PhoneExtractor,
    SkillExtractor,
)


class ResumeParser:

    def __init__(self, text):
        self.text = text

    def parse(self):

        resume = Resume()

        resume.raw_text = self.text

        resume.name = NameExtractor.extract(self.text)
        resume.email = EmailExtractor.extract(self.text)
        resume.phone = PhoneExtractor.extract(self.text)
        resume.skills = SkillExtractor.extract(self.text)

        return resume