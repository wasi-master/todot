"""Parses todos from source files"""
import re

from .todo import Todo


class Parser:
    """A class for reading and parsing todos from files"""

    default_tags = ("TODO", "FIXME", "BUG", "HACK", "UNDONE", "XXX")

    def __init__(self, files, *, tags=None):
        self.files = files
        self.tags = tags
        re_tags = "|".join(tags or self.default_tags)

        self.regex = re.compile(
            r"(//|\#|<--|<!--|/\*|;|--)\s*"            # comment start (required)
            rf"(?P<tag>{re_tags})\s*"                  # valid tags (required)
            r"\(?(?P<associates>[A-Za-z0-9@#, ]*)\)?"  # people assigned (optional)
            r"\s*[-:~,]"                               # separator: a hyphen, colon, comma, dot or tilde (required)
            r"\s*(?P<text>.*)"                         # text (required)
            r"\s*(-->|\*/)?",                          # comment end (optional)
            re.IGNORECASE,  # Ignore the case whether it's todo or TODO.
        )
        self.todos = []

    def parse(self):
        """Does the actual parsing"""
        for file in self.files:
            with open(file, encoding="utf-8") as f:
                lines = f.read().splitlines()
                for linepos, line in enumerate(lines, 1):
                    match = self.regex.search(line)
                    if not match:
                        continue
                    self.todos.append(Todo(match, file_name=file, linepos=linepos))
        return self.todos
