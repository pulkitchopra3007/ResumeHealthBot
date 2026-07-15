"""
Resume Data Model
"""

from dataclasses import dataclass, field


@dataclass
class Resume:

    # Contact
    name: str | None = None
    email: str | None = None
    phone: str | None = None
    location: str | None = None

    # Links
    linkedin: str | None = None
    github: str | None = None
    portfolio: str | None = None

    # Sections
    summary: str | None = None

    skills: list = field(default_factory=list)
    education: list = field(default_factory=list)
    experience: list = field(default_factory=list)
    projects: list = field(default_factory=list)
    certifications: list = field(default_factory=list)
    achievements: list = field(default_factory=list)
    languages: list = field(default_factory=list)

    # Metadata
    raw_text: str = ""