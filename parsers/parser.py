"""
Base Parser

Every parser in this project must inherit from this class.
"""


class DocumentParser:

    def parse(self, file_path):
        raise NotImplementedError("Parser not implemented.")