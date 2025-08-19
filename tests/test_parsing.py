"""Tests for the Parser class"""
import tempfile
import os
from todot.parser import Parser


def test_parser_initialization():
    """Test Parser initialization with default and custom tags"""
    files = ["test.py"]

    # Test default tags
    parser = Parser(files)
    assert parser.files == files
    assert parser.tags is None
    assert "TODO" in str(parser.regex.pattern)
    assert "FIXME" in str(parser.regex.pattern)
    assert "BUG" in str(parser.regex.pattern)

    # Test custom tags
    custom_tags = ["CUSTOM", "NOTE"]
    parser = Parser(files, tags=custom_tags)
    assert parser.tags == custom_tags
    assert "CUSTOM" in str(parser.regex.pattern)
    assert "NOTE" in str(parser.regex.pattern)


def test_parser_basic_todo_parsing():
    """Test parsing basic TODO comments"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write("# TODO: This is a test todo\n")
        f.write("// FIXME: This needs to be fixed\n")
        f.write("/* BUG: There is a bug here */\n")
        f.flush()

        try:
            parser = Parser([f.name])
            todos = parser.parse()

            assert len(todos) == 3

            # Check first TODO
            assert todos[0].tag == "TODO"
            assert todos[0].text == "This is a test todo"
            assert todos[0].linepos == 1
            assert todos[0].file_name.endswith(".py")

            # Check FIXME
            assert todos[1].tag == "FIXME"
            assert todos[1].text == "This needs to be fixed"
            assert todos[1].linepos == 2

            # Check BUG (note: the */ is captured as part of text due to regex behavior)
            assert todos[2].tag == "BUG"
            assert todos[2].text == "There is a bug here */"
            assert todos[2].linepos == 3

        finally:
            os.unlink(f.name)


def test_parser_with_associates():
    """Test parsing TODOs with associates/assignees"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write("# TODO(john, jane): Fix this issue\n")
        f.write("// FIXME(alice) - Update documentation\n")
        f.write("/* TODO: No assignee here */\n")
        f.flush()

        try:
            parser = Parser([f.name])
            todos = parser.parse()

            assert len(todos) == 3

            # Check TODO with associates
            assert todos[0].tag == "TODO"
            assert todos[0].associates == ["john", "jane"]
            assert todos[0].text == "Fix this issue"

            # Check FIXME with single associate
            assert todos[1].tag == "FIXME"
            assert todos[1].associates == ["alice"]
            assert todos[1].text == "Update documentation"

            # Check TODO without associates (note: */ is part of text)
            assert todos[2].tag == "TODO"
            assert todos[2].associates == [""]
            assert todos[2].text == "No assignee here */"

        finally:
            os.unlink(f.name)


def test_parser_different_comment_styles():
    """Test parsing different comment styles"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write("# TODO: Hash style comment\n")
        f.write("// TODO: Double slash comment\n")
        f.write("/* TODO: Block comment */\n")
        f.write("<!-- TODO: HTML comment -->\n")
        f.write("; TODO: Semicolon comment\n")
        f.write("-- TODO: SQL style comment\n")
        f.flush()

        try:
            parser = Parser([f.name])
            todos = parser.parse()

            assert len(todos) == 6
            for todo in todos:
                assert todo.tag == "TODO"
                assert "comment" in todo.text

        finally:
            os.unlink(f.name)


def test_parser_case_insensitive():
    """Test that parsing is case insensitive for tags"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write("# todo: lowercase todo\n")
        f.write("# TODO: uppercase todo\n")
        f.write("# ToDo: mixed case todo\n")
        f.flush()

        try:
            parser = Parser([f.name])
            todos = parser.parse()

            assert len(todos) == 3
            for todo in todos:
                assert todo.tag.upper() == "TODO"

        finally:
            os.unlink(f.name)


def test_parser_multiple_files():
    """Test parsing multiple files"""
    files_content = [
        ("# TODO: First file todo\n", '.py'),
        ("// FIXME: Second file fixme\n", '.js'),
        ("/* BUG: Third file bug */\n", '.c')
    ]

    temp_files = []
    try:
        for content, suffix in files_content:
            with tempfile.NamedTemporaryFile(mode='w', suffix=suffix, delete=False) as f:
                f.write(content)
                temp_files.append(f.name)

        parser = Parser(temp_files)
        todos = parser.parse()

        assert len(todos) == 3
        assert todos[0].tag == "TODO"
        assert todos[1].tag == "FIXME"
        assert todos[2].tag == "BUG"

        # Check file names are different
        file_names = [todo.file_name for todo in todos]
        assert len(set(file_names)) == 3

    finally:
        for temp_file in temp_files:
            os.unlink(temp_file)


def test_parser_no_matches():
    """Test parser with file containing no TODOs"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write("print('Hello world')\n")
        f.write("x = 42\n")
        f.write("# This is just a regular comment\n")
        f.flush()

        try:
            parser = Parser([f.name])
            todos = parser.parse()

            assert len(todos) == 0

        finally:
            os.unlink(f.name)
