"""
Resume Extractors

All extractors used by ResumeParser live here.
"""

import re


class EmailExtractor:

    @staticmethod
    def extract(text: str):

        pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

        match = re.search(pattern, text)

        if match:
            return match.group()

        return "Not Found"


class PhoneExtractor:

    @staticmethod
    def extract(text: str):

        pattern = r"(\+91[\s-]?)?[6-9]\d{9}"

        match = re.search(pattern, text)

        if match:
            return match.group()

        return "Not Found"