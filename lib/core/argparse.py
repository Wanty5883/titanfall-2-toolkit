# SPL - Standard Python Libraries
from argparse import ArgumentParser
import sys


def argParser(argv=None):
    """
    This function parses the command line parameters and arguments
    """
    if not argv:
        argv = sys.argv

    parser = ArgumentParser()
    parser.add_argument(
        "--root-dir",
        dest="rootDirectory",
        action="store",
        required=True,
        help="Set the extracted VPK directory"
    )
    subparser = parser.add_subparsers(dest="command")
    subparser_wpn(subparser)

    args = parser.parse_args()

    argAction(args, parser)


def argAction(args, parser):
    pass


def subparser_wpn(subparser):
    parser_wpn = subparser.add_parser("wpn", help="Weapons")
    parser_wpn.set_defaults(parser_wpn=True)
