"""Prints todos to various outputs and formats"""
from typing import List

from .todo import Todo

try:
    import rich
except ImportError:
    rich = None


class ConsolePrinter:
    """Prints todos to the console"""

    def __init__(self, todos: List[Todo]):
        self.todos = todos
        self.to_print = []

    def format(self):
        """Formats the todos to be printable"""
        if not self.todos:
            print("No todos found.")
            return
        longest_name = max(self.todos, key=lambda t: len(f"{t.file_name}:{t.linepos} "))
        padding_size = len(f"{longest_name.file_name}:{longest_name.linepos} ")
        for todo in self.todos:
            associates = (" (" + ", ".join(todo.associates) + ")") if todo.associates else ""
            current_name = len(todo.file_name + str(todo.linepos) + " ")
            self.to_print.append(
                f"{todo.file_name}:{todo.linepos} "
                f"{' '*(padding_size-current_name)}{todo.tag}"
                f"{associates}: {todo.text}"
            )

    def print(self):
        """Does the actual printing"""
        self.format()
        for todo in self.to_print:
            print(todo)


class ColoredConsolePrinter:
    """Prints todos to the console"""

    def __init__(self, todos: List[Todo]):
        self.todos = todos
        self.to_print = []

    def format(self):
        """Formats the todos to be printable"""
        if not self.todos:
            print("No todos found.")
            return
        longest_name = max(self.todos, key=lambda t: len(f"{t.file_name}:{t.linepos} "))
        padding_size = len(f"{longest_name.file_name}:{longest_name.linepos} ")
        for todo in self.todos:
            associates = (" (" + ", ".join(todo.associates) + ")") if todo.associates else ""
            current_name = len(todo.file_name + str(todo.linepos) + " ")
            if rich:
                self.to_print.append(
                    f"[bold yellow]{todo.file_name}:{todo.linepos}[/]"
                    f"[bold green]{' '*(padding_size-current_name)}{todo.tag}[/]"
                    f"[bold cyan]{associates}[/]: {todo.text}"
                )
            else:
                self.to_print.append(
                    f"\x1b[1;33m{todo.file_name}:{todo.linepos}\x1b[0m "
                    f"\x1b[1;32m{' '*(padding_size-current_name)}{todo.tag}\x1b[0m"
                    f"\x1b[1;36m{associates}\x1b[0m: {todo.text}"
                )

    def print(self):
        """Does the actual printing"""
        self.format()
        for todo in self.to_print:
            if rich:
                rich.print(todo)
            else:
                print(todo)


class TextFilePrinter(ConsolePrinter):
    """Prints todos to a text file"""

    def __init__(self, todos: List[Todo], file_name: str):
        super().__init__(todos)
        self.file_name = file_name or "todo.txt"

    def print(self):
        self.format()
        with open(self.file_name, "w", encoding="utf-8") as file:
            for todo in self.to_print:
                file.write(todo + "\n")
        if self.todos:
            print(f"Successfully saved all todos to {self.file_name}")


class MarkdownFilePrinter(TextFilePrinter):
    """Prints todos to a markdown file"""

    def __init__(
        self,
        todos: List[Todo],
        file_name: str,
    ):
        super().__init__(todos, file_name or "TODO.md")

    def format(self):
        """Formats the todos to be printable"""
        if not self.todos:
            print("No todos found.")
            return
        self.to_print.append("# TODO.md\n")
        for todo in self.todos:
            associates = ", ".join("@" + i for i in todo.associates) if todo.associates else ""
            self.to_print.append(f"- {todo.text} #{todo.tag} {associates} ({todo.file_name}:{todo.linepos})  ")


class GithubFlavouredMarkdownFilePrinter(MarkdownFilePrinter):
    """Prints todos to a markdown file"""

    def __init__(self, todos: List[Todo], file_name: str, repo: str, branch: str = None):
        super().__init__(todos, file_name or "TODO.md")
        self.repo = repo
        self.branch = branch or "master"

    def format(self):
        """Formats the todos to be printable"""
        if not self.todos:
            print("No todos found.")
            return
        self.to_print.append("# TODO.md\n")

        for todo in self.todos:
            associates = ", ".join("@" + i for i in todo.associates) if todo.associates else ""
            if self.repo:
                filename = todo.file_name.replace("\\", "/")
                file = f"[{todo.file_name}:{todo.linepos}]({self.repo}/blob/{self.branch}/{filename}#L{todo.linepos})"
            else:
                file = f"{todo.file_name}:{todo.linepos}"
            self.to_print.append(f"- [ ] {todo.text} #{todo.tag} {associates} ({file})  ")
