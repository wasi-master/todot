"""Finds source files"""
import os
import re
from pathlib import Path
from typing import List, Union

import pathspec

from .constants import VALID_FILE_TYPES

__all__ = ("Finder",)


class Finder:
    """A class for finding source files"""

    def __init__(self, path=None, *, filetypes=None, exclude=None, gitignore=None):
        self.filetypes = filetypes or [
            item.replace("+", r"\+") for sublist in VALID_FILE_TYPES.values() for item in sublist
        ]
        self.path = Path(path or ".")
        self.exclude = exclude or []
        self.exclude.extend(("TODO.md", "todo.txt"))
        self.gitignore = gitignore or False
        self.valid_file_types = re.compile(rf".*\.({'|'.join(self.filetypes)})$")
        self.spec = None
        if self.gitignore:
            try:
                with open(".gitignore") as f:
                    gitignore_lines = f.read().splitlines()
                self.spec = pathspec.PathSpec.from_lines('gitignore', gitignore_lines)
            except (OSError, PermissionError, FileNotFoundError) as exc:
                print(f"Failed to read gitignore due to {exc}")

    def _find(self, path: Path) -> Union[List[str], None]:
        files_grabbed = []
        try:
            files = list(os.scandir(path))
        except (OSError, NotADirectoryError, PermissionError) as exc:
            print(f"Failed to find files due to {exc}")
            return []
            
        for file in files:
            if file.name.startswith("."):
                continue
                
            file_path = file.path.replace("\\", "/")
            if file_path.startswith("./"):
                file_path = file_path[2:]
                
            if file_path in self.exclude:
                continue
                
            if self.spec and self.spec.match_file(file_path):
                continue

            if file.is_dir():
                files_grabbed.extend(self._find(file.path))
            elif self.valid_file_types.match(file.name):
                files_grabbed.append(file.path)
                
        return files_grabbed

    def find(self):
        """Does the actual finding"""
        return self._find(self.path)
