"""Tests for the Printer classes"""
import tempfile
import os
from unittest.mock import patch, MagicMock
from todot.printer import (
    ConsolePrinter, ColoredConsolePrinter, TextFilePrinter,
    MarkdownFilePrinter, GithubFlavouredMarkdownFilePrinter
)
from todot.todo import Todo


def create_mock_todo(tag="TODO", text="Test todo", file_name="test.py", linepos=1, associates=None):
    """Helper function to create a mock Todo object"""
    mock_match = MagicMock()
    mock_match.group.side_effect = lambda key: {
        "tag": tag,
        "text": text,
        "associates": ",".join(associates) if associates else ""
    }.get(key, "")

    todo = Todo(mock_match, file_name=file_name, linepos=linepos)
    if associates:
        todo.associates = associates
    else:
        todo.associates = [""]

    return todo


def test_console_printer_initialization():
    """Test ConsolePrinter initialization"""
    todos = [create_mock_todo()]
    printer = ConsolePrinter(todos)

    assert printer.todos == todos
    assert printer.to_print == []


def test_console_printer_empty_todos():
    """Test ConsolePrinter with empty todo list"""
    printer = ConsolePrinter([])

    with patch('builtins.print') as mock_print:
        printer.format()
        mock_print.assert_called_with("No todos found.")


def test_console_printer_format_and_print():
    """Test ConsolePrinter formatting and printing"""
    todos = [
        create_mock_todo(tag="TODO", text="First todo", file_name="file1.py", linepos=1),
        create_mock_todo(tag="FIXME", text="Second todo", file_name="file2.py", linepos=5)
    ]
    printer = ConsolePrinter(todos)

    with patch('builtins.print') as mock_print:
        printer.print()

        # Verify print was called (format() should be called inside print())
        assert mock_print.call_count >= 2  # At least 2 todos printed


def test_console_printer_with_associates():
    """Test ConsolePrinter with todos that have associates"""
    todo_with_associates = create_mock_todo(
        tag="TODO",
        text="Fix this issue",
        file_name="test.py",
        linepos=1,
        associates=["john", "jane"]
    )
    printer = ConsolePrinter([todo_with_associates])
    printer.format()

    assert len(printer.to_print) == 1
    printed_line = printer.to_print[0]
    assert "TODO" in printed_line
    assert "Fix this issue" in printed_line
    assert "john, jane" in printed_line


def test_colored_console_printer_initialization():
    """Test ColoredConsolePrinter initialization"""
    todos = [create_mock_todo()]
    printer = ColoredConsolePrinter(todos)

    assert printer.todos == todos
    assert printer.to_print == []


def test_colored_console_printer_without_rich():
    """Test ColoredConsolePrinter when rich is not available"""
    todos = [create_mock_todo(tag="TODO", text="Test todo", file_name="test.py", linepos=1)]
    printer = ColoredConsolePrinter(todos)

    # Mock rich to be None (not available)
    with patch('todot.printer.rich', None):
        printer.format()

        assert len(printer.to_print) == 1
        printed_line = printer.to_print[0]
        # Should contain ANSI color codes when rich is not available
        assert "\x1b[" in printed_line


def test_colored_console_printer_with_rich():
    """Test ColoredConsolePrinter when rich is available"""
    todos = [create_mock_todo(tag="TODO", text="Test todo", file_name="test.py", linepos=1)]
    printer = ColoredConsolePrinter(todos)

    # Mock rich to be available
    mock_rich = MagicMock()
    with patch('todot.printer.rich', mock_rich):
        printer.format()

        assert len(printer.to_print) == 1
        printed_line = printer.to_print[0]
        # Should contain rich markup when rich is available
        assert "[bold yellow]" in printed_line or "[/" in printed_line


def test_text_file_printer():
    """Test TextFilePrinter functionality"""
    todos = [
        create_mock_todo(tag="TODO", text="First todo", file_name="test.py", linepos=1),
        create_mock_todo(tag="FIXME", text="Second todo", file_name="test.py", linepos=2)
    ]

    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        try:
            printer = TextFilePrinter(todos, temp_file.name)

            with patch('builtins.print'):  # Suppress success message
                printer.print()

            # Read the file content
            with open(temp_file.name, 'r') as f:
                content = f.read()

            assert "TODO" in content
            assert "FIXME" in content
            assert "First todo" in content
            assert "Second todo" in content

        finally:
            os.unlink(temp_file.name)


def test_text_file_printer_empty_todos():
    """Test TextFilePrinter with empty todo list"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        try:
            printer = TextFilePrinter([], temp_file.name)

            with patch('builtins.print') as mock_print:
                printer.print()
                mock_print.assert_called_with("No todos found.")

        finally:
            os.unlink(temp_file.name)


def test_markdown_file_printer():
    """Test MarkdownFilePrinter functionality"""
    todos = [
        create_mock_todo(tag="TODO", text="First todo", file_name="test.py", linepos=1),
        create_mock_todo(tag="FIXME", text="Second todo", file_name="test.js", linepos=5, associates=["user1"])
    ]

    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as temp_file:
        try:
            printer = MarkdownFilePrinter(todos, temp_file.name)

            with patch('builtins.print'):  # Suppress success message
                printer.print()

            # Read the file content
            with open(temp_file.name, 'r') as f:
                content = f.read()

            assert "# TODO.md" in content
            assert "- First todo #TODO" in content
            assert "- Second todo #FIXME @user1" in content
            assert "(test.py:1)" in content
            assert "(test.js:5)" in content

        finally:
            os.unlink(temp_file.name)


def test_github_flavoured_markdown_printer():
    """Test GithubFlavouredMarkdownFilePrinter functionality"""
    todos = [
        create_mock_todo(tag="TODO", text="First todo", file_name="test.py", linepos=1),
        create_mock_todo(tag="BUG", text="Fix bug", file_name="src/main.py", linepos=10, associates=["dev1", "dev2"])
    ]

    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as temp_file:
        try:
            repo_url = "https://github.com/user/repo"
            printer = GithubFlavouredMarkdownFilePrinter(todos, temp_file.name, repo=repo_url, branch="main")

            with patch('builtins.print'):  # Suppress success message
                printer.print()

            # Read the file content
            with open(temp_file.name, 'r') as f:
                content = f.read()

            assert "# TODO.md" in content
            assert "- [ ] First todo #TODO" in content
            assert "- [ ] Fix bug #BUG @dev1, @dev2" in content

            # Check for GitHub links
            assert f"{repo_url}/blob/main/test.py#L1" in content
            assert f"{repo_url}/blob/main/src/main.py#L10" in content

        finally:
            os.unlink(temp_file.name)


def test_github_flavoured_markdown_printer_no_repo():
    """Test GithubFlavouredMarkdownFilePrinter without repo URL"""
    todos = [create_mock_todo(tag="TODO", text="Test todo", file_name="test.py", linepos=1)]

    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as temp_file:
        try:
            printer = GithubFlavouredMarkdownFilePrinter(todos, temp_file.name, repo=None)

            with patch('builtins.print'):  # Suppress success message
                printer.print()

            # Read the file content
            with open(temp_file.name, 'r') as f:
                content = f.read()

            # Should use plain file references without links
            assert "(test.py:1)" in content
            assert "http" not in content  # No HTTP links

        finally:
            os.unlink(temp_file.name)


def test_printer_default_filenames():
    """Test that printers use default filenames when none provided"""
    todos = [create_mock_todo()]

    # Test TextFilePrinter default
    with patch('builtins.open', create=True) as mock_open:
        with patch('builtins.print'):
            printer = TextFilePrinter(todos, None)
            printer.print()
            # Should use default filename
            mock_open.assert_called_with("todo.txt", "w", encoding="utf-8")

    # Test MarkdownFilePrinter default
    with patch('builtins.open', create=True) as mock_open:
        with patch('builtins.print'):
            printer = MarkdownFilePrinter(todos, None)
            printer.print()
            # Should use default filename
            mock_open.assert_called_with("TODO.md", "w", encoding="utf-8")
