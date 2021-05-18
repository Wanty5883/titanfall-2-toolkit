# SPL - Standard Python Libraries
from inspect import isclass
import hashlib
import os.path
# LPL - Local Python Libraries
from lib.core.enums import WPN
import lib.core.enums as ENUMS
import lib.r2.wpn_enums as ENUMS_WPN


def wpn_hashMDL_1P(rootDir, weapon):
    """
    Identify a given 1P weapon model file no matter the name in
    order to do modification accordingly even if user did
    model swap. Hence the reason of the md5 hash.
    Weapon var has to be a class name from "wpn_enums.py".
    """
    enums_classes = [x for x in dir(ENUMS) if isclass(getattr(ENUMS, x))]
    wpn_classes = [x for x in dir(ENUMS_WPN) if isclass(getattr(ENUMS_WPN, x))]
    # Negate "enums.py" classes from wpn_classes
    wpn_enums = [x for x in wpn_classes if x not in enums_classes]

    if weapon in wpn_enums:
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
                    return([weapon, x, WPN.VERSION_V1])
            return(WPN.VERSION_UNKNOWN)  # if file have unknown modification.
        else:
            return(WPN.VERSION_FILE404)  # if file does not exist.
