# SPL - Standard Python Libraries
from pathlib import Path
from shutil import copyfile
import glob
import hashlib
import json
import ntpath
import os
import os.path
import sys
# TPL - Third Party Libraries
from fastapi import HTTPException
# LPL - Local Python Libraries
from backend import ROOT_DIR
from lib.core.attr import attr_wpnList
from lib.core.enums import DATA
from lib.core.enums import NETWORK
from lib.core.enums import WPN
from lib.core.fs import fs_backupFile
from lib.core.http import getWeaponSkinInfo
from lib.core.http import getWeaponSkinMat
from lib.core.log import logger as logs
import lib.r2.wpn_enums as WPN_ENUMS


def wpn_hashMDL(rootDir, fileType, fileTarget):
    """
    Identify a given 1P weapon model file no matter the name in
    order to do modification accordingly even if user did
    model swap. Hence the reason of the md5 hash.
    Weapon var has to be a class name from "wpn_enums.py".
    """
    if fileType == WPN.FILE_TYPE_1P:  # Attributes for first person model
        fileType = "MDL_1P_FILE"
        fileFolder = "MDL_1P_FOLDER"
        hashVanilla = "MDL_1P_VANILLA_HASH"
        hashV1 = "MDL_1P_V1_HASH"
    elif fileType == WPN.FILE_TYPE_3P:  # Attribute for third person model
        fileType = None
    elif fileType == WPN.FILE_TYPE_HP:  # Attribute for holster view model
        fileType = None
    elif fileType == WPN.FILE_TYPE_MP:  # Attribute for menus view model
        fileType = None
    else:  # Just a bulletproof, argparse prevent that
        print("Error")  # TODO proper logging
        sys.exit(0)
    if not fileType:  # Bulletproof
        sys.exit(0)

    wpn_enums = attr_wpnList()  # List of classes name for getattr()
    fileName = getattr(getattr(WPN_ENUMS, fileTarget), fileType)
    fileFolder = getattr(getattr(WPN_ENUMS, fileTarget), fileFolder)
    filePath = "{0}\\{1}\\{2}".format(rootDir, fileFolder, fileName)
    if os.path.isfile(filePath):  # if file exist
        with open(filePath, "rb") as file:   # Get file hash
            file_byte = file.read()
            file_hash = hashlib.md5(file_byte).hexdigest()
        for x in wpn_enums:
            if file_hash == getattr(getattr(WPN_ENUMS, x), hashVanilla):
                result = [fileTarget.lower(), x.lower(), WPN.VERSION_VANILLA]
                logs.debug(result)
                return(result)
            elif file_hash == getattr(getattr(WPN_ENUMS, x), hashV1):
                result = [fileTarget.lower(), x.lower(), WPN.VERSION_1]
                logs.debug(result)
                return(result)
        result = WPN.FILE_UNKNOWN  # if file have unknown modification.
        logs.debug(result)
        return(result)
    elif not os.path.isfile(filePath):  # if file does not exist.
        result = WPN.FILE_404
        logs.debug(result)
        return(result)


def wpn_convertMDL(rootDir, fileType, fileVersion, fileTarget, structTarget=False):
    """
    Edit a given model file, 'fileTarget' being the attribute to get the
    file name and path, while 'structTarget' is the attribute to get which
    binaries to edit. Both 'fileTarget' and 'structTarget' can be the same, being
    usefull when model swap has been done on the given file.
    """
    if not structTarget:
        structTarget = fileTarget
    if fileType == WPN.FILE_TYPE_1P:
        fileName = "MDL_1P_FILE"  # Attribute for first person model
        if fileVersion == WPN.VERSION_1:
            fileBinOperation = "MDL_1P_V1_BIN"  # Attribute for bin operation
            fileHash = "MDL_1P_V1_HASH"
        elif fileVersion == WPN.VERSION_VANILLA:
            fileBinOperation = "MDL_1P_V1_BIN_VANILLA"  # Attribute for bin operation
            fileHash = "MDL_1P_VANILLA_HASH"
        fileFolder = "MDL_1P_FOLDER"  # TODO make exception from here
    elif fileType == WPN.FILE_TYPE_3P:
        fileName = ""  # Attribute for third person model
    elif fileType == WPN.FILE_TYPE_HP:
        fileName = ""  # Attribute for holster view model
    elif fileType == WPN.TYPE_MP:
        fileName = ""  # Attribute for menus view model
    else:  # Just a bulletproof, argparse prevent that
        print("Error")  # TODO proper logging
        sys.exit(0)

    fileName = getattr(getattr(WPN_ENUMS, fileTarget), fileName)
    fileDir = getattr(getattr(WPN_ENUMS, fileTarget), fileFolder)
    filePath = "{0}\\{1}\\{2}".format(rootDir, fileDir, fileName)
    fileMod = getattr(getattr(WPN_ENUMS, structTarget), fileBinOperation)
    try:
        with open(filePath, "r+b") as file:
            file_byte = file.read()
            file_hash = hashlib.md5(file_byte).hexdigest()
            if not file_hash == getattr(getattr(WPN_ENUMS, structTarget), fileHash):
                logs.error("The file structure does not correspond to the correct file hash")
                return(NETWORK.MESSAGE_ERROR)
            for offset, bytes in fileMod:
                file.seek(offset)
                file.write(bytes)
    except FileNotFoundError as error:
        errorMsg = "wpn_convertMDL() file not found: {0}".format(filePath)
        logs.debug(errorMsg)
        logs.debug(format(AttributeError))
        logs.debug(format(error))
        return(NETWORK.MESSAGE_ERROR)
    return(NETWORK.MESSAGE_SUCCESS)


def wpn_backupMDL(rootDir, fileType, fileTarget):
    """
    Manage the backup of a weapon model file
    First check if a backup already has been made, then
    check if the model file hash is correct to then check
    if the model file has been swapped with another one before
    the backup.
    """
    if fileType == WPN.FILE_TYPE_1P:
        backupFile = getattr(getattr(WPN_ENUMS, fileTarget), "MDL_1P_FILE")
        backupFolder = getattr(getattr(WPN_ENUMS, fileTarget), "MDL_1P_FOLDER")
    elif fileType == WPN.FILE_TYPE_3P:
        pass
    elif fileType == WPN.FILE_TYPE_HP:
        pass
    elif fileType == WPN.TYPE_MP:
        pass
    backupPath = r"{0}\{1}\{2}".format(rootDir, backupFolder, backupFile)
    # If a backup file already has been made
    if os.path.isfile(backupPath):
        return(NETWORK.MESSAGE_SUCCESS)

    hashData = wpn_hashMDL(rootDir, fileType, fileTarget)
    # If the file hash is unknown or error
    if hashData == (WPN.FILE_UNKNOWN or WPN.FILE_404):
        logs.critical("Weapon hash is either unknown or has an error")
        logs.critical(hashData)
        return({"error": hashData})
    # If the model file has been swapped with another one
    fileStruct = hashData[1]
    if fileStruct != getattr(getattr(WPN_ENUMS, fileTarget), "WPN_NAME_SHORT"):
        # TODO if this error occurs, prompt the users to backup the original file manually
        # Will also need to change the result message in order to do that
        logs.error("Cannot backup the file because it has been swapped with another one.")
        return {"result": NETWORK.MESSAGE_ERROR}

    fs_backupFile(backupPath)
    return(NETWORK.MESSAGE_SUCCESS)


def wpn_installSkin(materialDir, weaponName, skinID):
    # XXX Will only delete the materials used by the target skin. Will not remove other
    # materials if they are not in the desired skin.
    filePath = r"{0}\{1}\{2}".format(DATA.WEAPON_SKIN, weaponName, skinID)
    fileInfoPath = r"{0}\{1}".format(filePath, DATA.FILE_JSON_INFO)
    infoAPI = getWeaponSkinInfo(weaponName, skinID)
    # If folders exists, create otherwise
    if not os.path.isdir(filePath):
        os.makedirs(filePath)
    # If not connected to NoSkill server
    if "error" in infoAPI:
        # Raise error if there is no local files (materials)
        if not Path(fileInfoPath).is_file():
            raise HTTPException(status_code=503, detail="Service Unavailable")
        # If local files are present (check for "info.json")
        elif Path(fileInfoPath).is_file():
            with open(fileInfoPath, "r") as file:
                infoLocal = json.load(file)
            # Check if all the files are present
            for filePath in infoLocal["files"]:
                materialPath = r"{0}\data\{1}".format(ROOT_DIR, filePath)
                if not Path(materialPath).is_file():
                    raise HTTPException(status_code=409, detail="Missing some material files")
            # Copying the materials over the VPK folder
            for filePath in infoLocal["files"]:
                materialName = ntpath.basename(filePath)
                materialPath = r"{0}\data\{1}".format(ROOT_DIR, filePath).replace("/", "\\")
                materialDest = r"{0}\{1}".format(materialDir, materialName)
                # Remove file & copy the new one
                if Path(materialDest).is_file():
                    os.remove(materialDest)
                copyfile(materialPath, materialDest)
            return
    # If connected to NoSkill server
    elif "error" not in infoAPI:
        infoAPIjson = json.loads(infoAPI.text)
        # If "info.json" does not exist
        if not Path(fileInfoPath).is_file():
            with open(fileInfoPath, "w") as file:
                file.write(infoAPI.text)
        # If "info.json" exist already
        if Path(fileInfoPath).is_file():
            with open(fileInfoPath, "r") as file:
                infoLocal = json.load(file)
            # If skin version are identical (compared to the NoSkill API)
            if infoLocal["skinVersion"] == infoAPIjson["skinVersion"]:
                for filePath in infoLocal["files"]:
                    materialName = ntpath.basename(filePath)
                    materialPath = r"{0}\data\{1}".format(ROOT_DIR, filePath).replace("/", "\\")
                    materialDest = r"{0}\{1}".format(materialDir, materialName)
                    # Download the missing file
                    if not Path(materialPath).is_file():
                        materialFile = getWeaponSkinMat(filePath)
                        open(materialPath, "wb").write(materialFile.content)
                    # Remove file & copy the new one
                    if Path(materialDest).is_file():
                        os.remove(materialDest)
                    copyfile(materialPath, materialDest)
                return
            # If skin version is different (compare to the NoSkill API)
            elif infoLocal["skinVersion"] != infoAPIjson["skinVersion"]:
                # Delete all the files for this skin except "info.json"
                if os.path.isfile(fileInfoPath):
                    materialPurge = glob.glob("{0}\\*.*".format(filePath))
                    materialPurge.remove(fileInfoPath)
                    for materialPrune in materialPurge:
                        os.remove(materialPrune)
                # Update "info.json" with up to date response from NoSkill API
                with open(fileInfoPath, "w") as file:
                    file.write(infoAPI.text)
                for filePath in infoLocal["files"]:
                    materialName = ntpath.basename(filePath)
                    materialPath = r"{0}\data\{1}".format(ROOT_DIR, filePath).replace("/", "\\")
                    materialDest = r"{0}\{1}".format(materialDir, materialName)
                    # Download the missing file
                    if not Path(materialPath).is_file():
                        materialFile = getWeaponSkinMat(filePath)
                        open(materialPath, "wb").write(materialFile.content)
                return
    # return(json.loads(result.text))
