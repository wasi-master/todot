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

    def _find(self, path: Path) -> Union[List[str], None]:
        files_grabbed = []
        try:
            files = list(os.scandir(path))
        except (OSError, NotADirectoryError, PermissionError) as exc:
            print(f"Failed to find files due to {exc}")
            return
        if self.gitignore:
            try:
                with open(".gitignore") as f:
                    gitignore = f.read().splitlines()
            except (OSError, PermissionError, FileNotFoundError) as exc:
                print(f"Failed to read gitignore due to {exc}")
                return
            else:
                formatted_files = [i.path.replace("\\", "/").replace("./","") for i in files]
                spec = pathspec.PathSpec.from_lines(pathspec.patterns.GitWildMatchPattern, gitignore)
                ignore_files = list(spec.match_files(formatted_files))
                self.exclude.extend(ignore_files)
        for file in files:
            if any(i.startswith(".") for i in file.name.replace("\\", "/").split("/")):
                continue
            if file.path.replace("\\", "/").lstrip("/.") in self.exclude:
                continue
            if file.is_dir():
                files_grabbed.extend(self._find(file.path))
            if not self.valid_file_types.match(file.name):
                continue
            files_grabbed.append(file.path)
        return files_grabbed

    def find(self):
        """Does the actual finding"""
        return self._find(self.path)
