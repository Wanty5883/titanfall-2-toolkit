# SPL - Standard Python Libraries
import hashlib
import os.path
import sys
# LPL - Local Python Libraries
from lib.core.enums import WPN
from lib.core.attr import attr_wpnList
import lib.r2.wpn_enums as ENUMS_WPN


def wpn_hashMDL_1P(rootDir, weapon):
    """
    Identify a given 1P weapon model file no matter the name in
    order to do modification accordingly even if user did
    model swap. Hence the reason of the md5 hash.
    Weapon var has to be a class name from "wpn_enums.py".
    """
    wpn_enums = attr_wpnList()

    if weapon in wpn_enums:  # Just a bulletproof, argparse prevent that
        fileName = getattr(getattr(ENUMS_WPN, weapon), "MDL_FILE_1P")
        filePath = getattr(getattr(ENUMS_WPN, weapon), "MDL_FOLDER")
        file1P = "{0}\\{1}\\{2}".format(rootDir, filePath, fileName)
        if os.path.isfile(file1P):  # if file exist
            with open(file1P, "rb") as file:   # Get file hash
                file_byte = file.read()
                file_hash = hashlib.md5(file_byte).hexdigest()
            for x in wpn_enums:
                hashVanilla = "MDL_VANILLA_1P_HASH"
                hashV1 = "MDL_V1_1P_HASH"
                if file_hash == getattr(getattr(ENUMS_WPN, x), hashVanilla):
                    return([weapon, x, WPN.VERSION_VANILLA])
                elif file_hash == getattr(getattr(ENUMS_WPN, x), hashV1):
                    return([weapon, x, WPN.VERSION_1])
            return(WPN.VERSION_UNKNOWN)  # if file have unknown modification.
        else:
            return(WPN.VERSION_FILE404)  # if file does not exist.


def wpn_convertMDL(rootDir, fileType, fileVersion, fileTarget, structTarget):
    """
    Edit a given model file, 'fileTarget' being the attribute to get the
    file name and path, while 'structTarget' is the attribute to get which
    binaries to edit. Both 'fileTarget' and 'structTarget' can be the same, being
    usefull when model swap has been done on the given file.
    """
    if fileType == WPN.TYPE_1P:
        fileType = "MDL_FILE_1P"  # Attribute for first person model
        if fileVersion == WPN.VERSION_1:
            fileVersion = "MDL_V1_1P"  # Attribute for bin operation
        elif fileVersion == WPN.VERSION_VANILLA:
            fileVersion = "MDL_V1_1P_VANILLA"  # Attribute for bin operation
        fileFolder = "MDL_FOLDER"  # TODO make exception from here
    elif fileType == WPN.TYPE_3P:
        fileType = "MDL_FILE_3P"  # Attribute for third person model
    elif fileType == WPN.TYPE_HP:
        fileType = "MDL_FILE_HP"  # Attribute for holster view model
    elif fileType == WPN.TYPE_MP:
        fileType = "MDL_FILE_MP"  # Attribute for menus view model
    else:  # Just a bulletproof, argparse prevent that
        print("Error")  # TODO proper logging
        sys.exit(0)

    fileName = getattr(getattr(ENUMS_WPN, fileTarget), fileType)
    fileDir = getattr(getattr(ENUMS_WPN, fileTarget), fileFolder)
    filePath = "{0}\\{1}\\{2}".format(rootDir, fileDir, fileName)
    fileMod = getattr(getattr(ENUMS_WPN, structTarget), fileVersion)
    with open(filePath, "r+b") as file:
        for offset, bytes in fileMod:
            file.seek(offset)
            file.write(bytes)
