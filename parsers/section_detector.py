"""
Resume Section Detector
"""

import re


class SectionDetector:

    SECTION_HEADERS = {
        "education": [
            "education",
            "academic background",
            "qualification",
            "qualifications",
        ],
        "experience": [
            "experience",
            "work experience",
            "professional experience",
            "employment",
        ],
        "skills": [
            "skills",
            "technical skills",
            "core skills",
            "key skills",
        ],
        "projects": [
            "projects",
            "academic projects",
            "personal projects",
        ],
        "certifications": [
            "certifications",
            "certificates",
            "licenses",
        ],
    }

    def __init__(self, text):
        self.text = text

    def detect(self):

        sections = {}

        lower_text = self.text.lower()

        for section_name, headers in self.SECTION_HEADERS.items():

            for header in headers:

                pattern = rf"{header}\s*\n"

                match = re.search(pattern, lower_text)

                if match:

                    sections[section_name] = match.start()

                    break

        return sections