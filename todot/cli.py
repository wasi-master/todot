import argparse
import re

from . import __version__

GITHUB_REGEX = r"^https://(www\.)?github\.com/(?P<name>[a-z\d](?:[a-z\d]|-(?=[a-z\d])){0,38})/(?P<repo>[A-Za-z-_]{0,100})$"
def github_repo(arg_value):
    pattern = re.compile(GITHUB_REGEX)
    if not pattern.match(arg_value):
        raise argparse.ArgumentTypeError('Invalid github repository url')
    return arg_value
def github_repo_branch(arg_value):
    if not re.match(r'\w{0,28}',arg_value):
        raise argparse.ArgumentTypeError('Invalid github repository url')
    return arg_value

argparser = argparse.ArgumentParser(
    prog="todot",
    usage="%(prog)s path [options] ",
    description="A powerful tool to parse TODOs/FIXMEs etc. from source files",
    epilog="Enjoy the program! :)",
)

argparser.add_argument("path", metavar="path", type=str, nargs="?", help="specify a path to list todos from")
argparser.add_argument("--version", action="store_true")
argparser.add_argument(
    "--output",
    action="store",
    metavar="file",
    type=str,
    required=False,
    default=None,
    help="specify a file to write the output to, by default stdout",
)
argparser.add_argument(
    "--format",
    action="store",
    metavar="printer",
    type=str,
    required=False,
    default="default",
    help="specify a format to create the output using",
)
argparser.add_argument("--configfile", default=None, help="file to read the config from")
argparser.add_argument(
    "--ignore",
    "--exclude",
    metavar="file1,file2...",
    type=str,
    required=False,
    default=None,
    help="comma delimited list input of files to ignore",
)
argparser.add_argument(
    "--gitignore",
    action="store_true",
    help="if used, ignores files in .gitignore",
)
argparser.add_argument(
    "--tags",
    metavar="tag1,tag2...",
    type=str,
    required=False,
    default=None,
    help="comma delimited list input of extra tags to parse",
)
argparser.add_argument(
    "--repo",
    action="store",
    metavar="repository_url",
    type=github_repo,
    required=False,
    default=None,
    help="specify a github repository to add hyperlinks to",
)
argparser.add_argument(
    "--branch",
    action="store",
    metavar="repository_branch",
    type=github_repo_branch,
    required=False,
    default=None,
    help="specify a github repository branch to add hyperlinks to, by default master",
)

