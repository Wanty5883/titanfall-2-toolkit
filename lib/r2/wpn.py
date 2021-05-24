# SPL - Standard Python Libraries
import hashlib
import os.path
import sys
# LPL - Local Python Libraries
from lib.core.attr import attr_wpnList
from lib.core.enums import WPN
from lib.core.log import logger
import lib.r2.wpn_enums as ENUMS_WPN


def wpn_hashMDL(rootDir, fileType, fileTarget):
    """
    Identify a given 1P weapon model file no matter the name in
    order to do modification accordingly even if user did
    model swap. Hence the reason of the md5 hash.
    Weapon var has to be a class name from "wpn_enums.py".
    """
    if fileType == WPN.TYPE_1P:
        fileType = "MDL_1P_FILE"  # Attribute for first person model
        hashVanilla = "MDL_1P_VANILLA_HASH"
        hashV1 = "MDL_1P_V1_HASH"
    elif fileType == WPN.TYPE_3P:
        fileType = ""  # Attribute for third person model
    elif fileType == WPN.TYPE_HP:
        fileType = ""  # Attribute for holster view model
    elif fileType == WPN.TYPE_MP:
        fileType = ""  # Attribute for menus view model
    else:  # Just a bulletproof, argparse prevent that
        print("Error")  # TODO proper logging
        sys.exit(0)
    fileFolder = "MDL_1P_FOLDER"
    wpn_enums = attr_wpnList()

    fileName = getattr(getattr(ENUMS_WPN, fileTarget), fileType)
    filePath = getattr(getattr(ENUMS_WPN, fileTarget), fileFolder)
    file1P = "{0}\\{1}\\{2}".format(rootDir, filePath, fileName)
    if os.path.isfile(file1P):  # if file exist
        with open(file1P, "rb") as file:   # Get file hash
            file_byte = file.read()
            file_hash = hashlib.md5(file_byte).hexdigest()
        for x in wpn_enums:
            if file_hash == getattr(getattr(ENUMS_WPN, x), hashVanilla):
                logger.debug([fileTarget, x, WPN.VERSION_VANILLA])
                return([fileTarget, x, WPN.VERSION_VANILLA])
            elif file_hash == getattr(getattr(ENUMS_WPN, x), hashV1):
                logger.debug([fileTarget, x, WPN.VERSION_1])
                return([fileTarget, x, WPN.VERSION_1])
        r = WPN.VERSION_UNKNOWN  # if file have unknown modification.
        logger.debug(r)
        return(r)
    else:
        r = WPN.VERSION_FILE404  # if file does not exist.
        logger.debug(r)
        return(r)


def wpn_convertMDL(rootDir, fileType, fileVersion, fileTarget, structTarget):
    """
    Edit a given model file, 'fileTarget' being the attribute to get the
    file name and path, while 'structTarget' is the attribute to get which
    binaries to edit. Both 'fileTarget' and 'structTarget' can be the same, being
    usefull when model swap has been done on the given file.
    """
    if fileType == WPN.TYPE_1P:
        fileName = "MDL_1P_FILE"  # Attribute for first person model
        if fileVersion == WPN.VERSION_1:
            fileBinOperation = "MDL_1P_V1_BIN"  # Attribute for bin operation
        elif fileVersion == WPN.VERSION_VANILLA:
            fileBinOperation = "MDL_V1_1P_VANILLA"  # Attribute for bin operation
        fileFolder = "MDL_1P_FOLDER"  # TODO make exception from here
    elif fileType == WPN.TYPE_3P:
        fileName = "MDL_FILE_3P"  # Attribute for third person model
    elif fileType == WPN.TYPE_HP:
        fileName = "MDL_FILE_HP"  # Attribute for holster view model
    elif fileType == WPN.TYPE_MP:
        fileName = "MDL_FILE_MP"  # Attribute for menus view model
    else:  # Just a bulletproof, argparse prevent that
        print("Error")  # TODO proper logging
        sys.exit(0)

    fileName = getattr(getattr(ENUMS_WPN, fileTarget), fileName)
    fileDir = getattr(getattr(ENUMS_WPN, fileTarget), fileFolder)
    filePath = "{0}\\{1}\\{2}".format(rootDir, fileDir, fileName)
    fileMod = getattr(getattr(ENUMS_WPN, structTarget), fileBinOperation)
    with open(filePath, "r+b") as file:
        for offset, bytes in fileMod:
            file.seek(offset)
            file.write(bytes)
