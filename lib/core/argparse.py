# SPL - Standard Python Libraries
from argparse import ArgumentParser
import sys
# LPL - Local Python Libraries
from lib.core.attr import attr_wpnList
from lib.core.enums import WPN
from lib.core.log import logger as logs
from lib.r2.wpn import wpn_hashMDL
from lib.r2.wpn import wpn_convertMDL


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
        help="Set the extracted VPK directory"
    )
    subparser = parser.add_subparsers(dest="command")
    subparser_wpn(subparser)

    args = parser.parse_args()

    argAction(args, parser)


def argAction(args, parser):
    logs.info(vars(args))  # Log the command arguments used
    if not args.command:  # Display help message if parser is not used
        parser.parse_args(["--help"])
        sys.exit(0)
    if args.command == "wpn":
        argSubaction_wpn(args, parser)


def subparser_wpn(subparser):
    parser_wpn = subparser.add_parser("wpn", help="Weapons")
    parser_wpn.set_defaults(parser_wpn=True)
    wpn_enums = attr_wpnList()  # Get wpn attribute names

    wpnMDL = parser_wpn.add_argument_group(
        "3D Models",
        "Commands for weapon 3D models (.mdl) file manipulation"
    )
    # Function arguments
    wpnMDL.add_argument(
        "--wpn-convertMDL",
        dest="wpnConvertMDL",
        action="store_true",
        help="Convert a weapon mdl to a defined version"
    )
    wpnMDL.add_argument(
        "--wpn-hashMDL",
        dest="wpnHashMDL",
        action="store_true",
        help="Hash a weapon model file"
    )
    # General arguments
    wpnMDL.add_argument(
        "--wpn-fileType",
        dest="wpnFileType",
        choices=[
            WPN.FILE_TYPE_1P,
            WPN.FILE_TYPE_3P,
            WPN.FILE_TYPE_HP,
            WPN.FILE_TYPE_MP
        ],
        help="Choose the 3D model file type (1P, 3P, etc.)"
    )
    wpnMDL.add_argument(
        "--wpn-fileVersion",
        dest="wpnFileVersion",
        choices=[
            WPN.VERSION_1,
            WPN.VERSION_2,
            WPN.VERSION_VANILLA,
        ],
        help="Choose the 3D model file version"
    )
    wpnMDL.add_argument(
        "--wpn-fileTarget",
        dest="wpnFileTarget",
        choices=wpn_enums,
        help="Choose the 3D model target file"
    )
    wpnMDL.add_argument(
        "--wpn-structTarget",
        dest="wpnStructTarget",
        choices=wpn_enums,
        help="Choose the 3D model struct target"
    )


def argSubaction_wpn(args, parser):
    if args.wpnConvertMDL:  # Convert weapon model file
        if not args.rootDirectory:
            logs.critical("Root directory not defined")
            sys.exit(0)
        if not args.wpnFileType:
            logs.critical("Weapon file type is not defined")
            sys.exit(0)
        if not args.wpnFileVersion:
            logs.critical("Weapon file version is not defined")
            sys.exit(0)
        if not args.wpnFileTarget:
            logs.critical("Weapon file target is not defined")
            sys.exit(0)
        if not args.wpnStructTarget:
            logs.critical("Weapon file structure is not defined")
            sys.exit(0)
        wpn_convertMDL(
            args.rootDirectory,
            args.wpnFileType,
            args.wpnFileVersion,
            args.wpnFileTarget,
            args.wpnStructTarget
        )
    if args.wpnHashMDL:  # Model MD5 hash
        if not args.rootDirectory:
            logs.critical("Root directory not defined")
            sys.exit(0)
        if not args.wpnFileType:
            logs.critical("Weapon file type is not defined")
            sys.exit(0)
        if not args.wpnFileTarget:
            logs.critical("Weapon file target is not defined")
            sys.exit(0)
        wpn_hashMDL(args.rootDirectory, args.wpnFileType, args.wpnFileTarget)
