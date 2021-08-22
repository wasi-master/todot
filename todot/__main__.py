"""CLI"""
import configparser
import os
import sys
import time

from . import __version__
from .cli import argparser
from .finder import Finder
from .parser import Parser
from .printer import (ColoredConsolePrinter, ConsolePrinter,
                      GithubFlavouredMarkdownFilePrinter, MarkdownFilePrinter,
                      TextFilePrinter)

PRINTER_MAPPING = {
    "default": ConsolePrinter,
    "color": ColoredConsolePrinter,
    "markdown": MarkdownFilePrinter,
    "text": TextFilePrinter,
    "github": GithubFlavouredMarkdownFilePrinter
}


def run():
    """Runs the CLI"""
    start = time.time()
    args = argparser.parse_args()
    if args.version:
        print(f"todot: {__version__}\npython: {sys.version}")
        return

    config = configparser.ConfigParser()
    if args.configfile:
        config.read(args.configfile)
    else:
        if os.path.exists(".todotrc"):
            config.read(".todotrc")
        else:
            config = {"TODOT": {}}
    for key, value in config["TODOT"].items():
        try:
            provided_value = getattr(args, key)
            if (not provided_value) or provided_value == "default":
                setattr(args, key, value)
        except AttributeError:
            setattr(args, key, value)

    exclude = [i.replace("\\", "/") for i in args.ignore.split(",")] if args.ignore else []
    tags = args.tags.split(",") if args.tags else None
    finder = Finder(args.path, exclude=exclude, gitignore=args.gitignore)
    found = finder.find()
    parser = Parser(found, tags=tags)
    todos = parser.parse()
    if args.format == "text" or args.output and args.output.endswith(".txt"):
        printer = TextFilePrinter(todos, file_name=args.output)
    elif args.format == "github":
        printer = GithubFlavouredMarkdownFilePrinter(todos, file_name=args.output, repo=args.repo, branch=args.branch)
    elif args.format == "markdown":
        printer = MarkdownFilePrinter(todos, file_name=args.output)
    else:
        printer = PRINTER_MAPPING.get(args.format, ConsolePrinter)(todos)
    printer.print()
    end = time.time()
    if end - start > 0.5:
        print(f"Took {round(end-start, 2)} seconds to complete")


if __name__ == "__main__":
    run()
