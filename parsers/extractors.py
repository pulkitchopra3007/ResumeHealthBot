"""
Resume Extractors
"""

import re
from pathlib import Path


class EmailExtractor:

    @staticmethod
    def extract(text):

        pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

        match = re.search(pattern, text)

        return match.group() if match else "Not Found"


class PhoneExtractor:

    @staticmethod
    def extract(text):

        pattern = r"(\+91[\s-]?)?[6-9]\d{9}"

        match = re.search(pattern, text)

        return match.group() if match else "Not Found"


class SkillExtractor:

    DATABASE = Path("database/skills.txt")

    @staticmethod
    def extract(text):

        if not SkillExtractor.DATABASE.exists():
            return []

        resume = text.lower()

        found = []

        with open(SkillExtractor.DATABASE, "r", encoding="utf-8") as file:

            for skill in file:

                skill = skill.strip()

                if skill and skill.lower() in resume:
                    found.append(skill)

        return sorted(set(found))