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


class NameExtractor:

    @staticmethod
    def extract(text):

        lines = [line.strip() for line in text.split("\n") if line.strip()]

        blacklist = {
            "resume",
            "curriculum vitae",
            "education",
            "experience",
            "skills",
            "projects",
            "contact",
            "summary",
            "certifications",
            "achievements",
        }

        for line in lines[:10]:

            lower = line.lower()

            if lower in blacklist:
                continue

            if "@" in line:
                continue

            if any(ch.isdigit() for ch in line):
                continue

            words = line.split()

            if 2 <= len(words) <= 4:
                return line.title()

        return "Not Found"


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
class LinkExtractor:

    @staticmethod
    def extract(text):

        import re

        pattern = r"(https?://[^\s]+|www\.[^\s]+|linkedin\.com/[^\s]+|github\.com/[^\s]+)"

        links = re.findall(pattern, text, flags=re.IGNORECASE)

        cleaned = []

        for link in links:

            link = link.strip(".,;()[]")

            if link not in cleaned:
                cleaned.append(link)

        return cleaned