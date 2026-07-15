"""
Resume Schema

Single source of truth for parsed resume data.
"""


class Resume:

    def __init__(self):
        self.name = None
        self.email = None
        self.phone = None

        self.summary = None

        self.skills = []
        self.education = []
        self.experience = []
        self.projects = []
        self.certifications = []

        self.links = []

        self.score = 0

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "summary": self.summary,
            "skills": self.skills,
            "education": self.education,
            "experience": self.experience,
            "projects": self.projects,
            "certifications": self.certifications,
            "links": self.links,
            "score": self.score,
        }