"""File for the todo class"""
from typing import Match


class Todo:
    """Class for managing TODOs"""
    def __init__(self, match: Match, *, file_name=None, linepos=None):
        self.match = match

        self.file_name = file_name.lstrip(".\\/")
        self.linepos = linepos

        self.tag = match.group("tag")
        self.text = match.group("text")
        self.associates = [i.strip() for i in match.group("associates").split(",")]

    def __repr__(self):
        return f"{self.file_name}:{self.linepos} {self.tag} {tuple(self.associates)}: {self.text}"
