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
    if fileType == WPN.TYPE_1P:  # Attributes for first person model
        fileType = "MDL_1P_FILE"
        fileFolder = "MDL_1P_FOLDER"
        hashVanilla = "MDL_1P_VANILLA_HASH"
        hashV1 = "MDL_1P_V1_HASH"
    elif fileType == WPN.TYPE_3P:  # Attribute for third person model
        fileType = None
    elif fileType == WPN.TYPE_HP:  # Attribute for holster view model
        fileType = None
    elif fileType == WPN.TYPE_MP:  # Attribute for menus view model
        fileType = None
    else:  # Just a bulletproof, argparse prevent that
        print("Error")  # TODO proper logging
        sys.exit(0)
    if not fileType:  # Bulletproof
        sys.exit(0)

    wpn_enums = attr_wpnList()  # List of classes name for getattr()
    fileName = getattr(getattr(ENUMS_WPN, fileTarget), fileType)
    fileFolder = getattr(getattr(ENUMS_WPN, fileTarget), fileFolder)
    filePath = "{0}\\{1}\\{2}".format(rootDir, fileFolder, fileName)
    if os.path.isfile(filePath):  # if file exist
        with open(filePath, "rb") as file:   # Get file hash
            file_byte = file.read()
            file_hash = hashlib.md5(file_byte).hexdigest()
        for x in wpn_enums:
            if file_hash == getattr(getattr(ENUMS_WPN, x), hashVanilla):
                result = [fileTarget, x, WPN.VERSION_VANILLA]
                logger.debug(result)
                return(result)
            elif file_hash == getattr(getattr(ENUMS_WPN, x), hashV1):
                result = [fileTarget, x, WPN.VERSION_1]
                logger.debug(result)
                return(result)
        result = WPN.FILE_UNKNOWN  # if file have unknown modification.
        logger.debug(result)
        return(result)
    elif not os.path.isfile(filePath):  # if file does not exist.
        result = WPN.FILE_404
        logger.debug(result)
        return(result)


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
            fileBinOperation = "MDL_1P_V1_BIN_VANILLA"  # Attribute for bin operation
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
