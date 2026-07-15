"""
Base Rule Class
"""


class Rule:

    def __init__(
        self,
        rule_id,
        title,
        description,
        severity,
    ):
        self.rule_id = rule_id
        self.title = title
        self.description = description
        self.severity = severity

    def check(self, resume):
        raise NotImplementedError