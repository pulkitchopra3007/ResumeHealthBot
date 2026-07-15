import re


class ResumeParser:
    def __init__(self, text: str):
        self.text = text

    def get_email(self):
        match = re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            self.text,
        )
        return match.group(0) if match else "Not Found"

    def get_phone(self):
        match = re.search(
            r"(\+91[\s-]?)?[6-9]\d{9}",
            self.text,
        )
        return match.group(0) if match else "Not Found"