# SPL - Standard Python Libraries
from pathlib import Path
from shutil import copyfile
import glob
import json
import ntpath
import os
# TPL - Third Party Libraries
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Query
# LPL - Local Python Libraries
from backend import ROOT_DIR
from lib.core.attr import attr_wpnList
from lib.core.enums import DATA
from lib.core.enums import WPN
from lib.core.http import getWeaponSkinInfo
from lib.core.http import getWeaponSkinMat
from lib.core.log import logger_api as logs
from lib.r2.wpn import wpn_backupMDL
from lib.r2.wpn import wpn_convertMDL
from lib.r2.wpn import wpn_hashMDL
import lib.r2.wpn_enums as WPN_ENUMS


app = FastAPI()
# APP = app

# $$\  $$\  $$\  $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$$\
# $$ | $$ | $$ |$$  __$$\  \____$$\ $$  __$$\ $$  __$$\ $$  __$$\
# $$ | $$ | $$ |$$$$$$$$ | $$$$$$$ |$$ /  $$ |$$ /  $$ |$$ |  $$ |
# $$ | $$ | $$ |$$   ____|$$  __$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |
# \$$$$$\$$$$  |\$$$$$$$\ \$$$$$$$ |$$$$$$$  |\$$$$$$  |$$ |  $$ |
#  \_____\____/  \_______| \_______|$$  ____/  \______/ \__|  \__|
#                                   $$ |
#                                   $$ |
#                                   \__|


@app.get("/weapons")
async def weaponList():
    """
    Return all weapons information in a form of a nested list. [{weapon1}, {weapon2}]
    The returned information are used place all the weapons in the main weapon
    window of the GUI including their name, icon, etc. It also return the weapon
    description used when a weapon is selected.
    """
    weapons = []
    for weapon in attr_wpnList():
        nameShort = getattr(getattr(WPN_ENUMS, weapon), "WPN_NAME_SHORT")
        weapons.append({
            "name": getattr(getattr(WPN_ENUMS, weapon), "WPN_NAME"),
            "nameShort": nameShort,
            "description": getattr(getattr(WPN_ENUMS, weapon), "WPN_DESC"),
            "description_long": getattr(getattr(WPN_ENUMS, weapon), "WPN_LONGDESC"),
            "class": getattr(getattr(WPN_ENUMS, weapon), "WPN_CLASS"),
            "type": getattr(getattr(WPN_ENUMS, weapon), "WPN_TYPE"),
            "iconName": "{}.png".format(nameShort),
            "iconPath": r"{}\{}.png".format(WPN.FILE_PATH_ICON, nameShort)
        })
    return(weapons)


@app.get("/weapon/convertmdl")
async def weaponConvertMDL(
    rootDirectory: str = Query(...),
    fileType: str = Query(...),
    fileVersion: str = Query(...),
    fileTarget: str = Query(...),
    structTarget: str = Query(...),
):
    # Check if arguments are correct
    # FILE TYPE
    conditions = [WPN.FILE_TYPE_1P, WPN.FILE_TYPE_3P, WPN.FILE_TYPE_HP, WPN.FILE_TYPE_MP]
    if fileType not in conditions:
        errorMsg = "Given file type is unknown"
        logs.critical("Internal API error: /weapon/convertmdl")
        logs.critical(errorMsg)
        logs.critical(fileType)
        return {"error": errorMsg}
    # FILE VERSION
    conditions = [WPN.VERSION_1, WPN.VERSION_2, WPN.VERSION_VANILLA]
    if fileVersion not in conditions:
        errorMsg = "Given file verison is unknown"
        logs.critical("Internal API error: /weapon/convertmdl")
        logs.critical(errorMsg)
        logs.critical(fileVersion)
        return {"error": errorMsg}
    # FILE TARGET
    if fileTarget.upper() not in attr_wpnList():
        errorMsg = "Given file target is unknown"
        logs.critical("Internal API error: /weapon/convertmdl")
        logs.critical(errorMsg)
        logs.critical(fileTarget)
        return {"error": errorMsg}
    # STRUCT TARGET
    if structTarget.upper() not in attr_wpnList():
        errorMsg = "Given struct target is unknown"
        logs.critical("Internal API error: /weapon/convertmdl")
        logs.critical(errorMsg)
        logs.critical(structTarget)
        return {"error": errorMsg}
    r = wpn_convertMDL(rootDirectory, fileType, fileVersion, fileTarget.upper(), structTarget.upper())
    return {"result": r}


@app.get("/weapon/hashmdl")
async def weaponHashMDL(
    rootDirectory: str = Query(...),
    fileType: str = Query(...),
    fileTarget: str = Query(...)
):
    # Check if arguments are correct
    # FILE TYPE
    conditions = [WPN.FILE_TYPE_1P, WPN.FILE_TYPE_3P, WPN.FILE_TYPE_HP, WPN.FILE_TYPE_MP]
    if fileType not in conditions:
        errorMsg = "Given file type is unknown"
        logs.critical("Internal API error: /weapon/hashmdl")
        logs.critical(errorMsg)
        logs.critical(fileType)
        return {"error": errorMsg}
    # FILE TARGET
    fileTarget = fileTarget.upper()
    if fileTarget not in attr_wpnList():
        errorMsg = "Given file target is unknown"
        logs.critical("Internal API error: /weapon/hashmdl")
        logs.critical(errorMsg)
        logs.critical(fileTarget)
        return {"error": errorMsg}

    hashData = wpn_hashMDL(rootDirectory, fileType, fileTarget)
    if hashData == (WPN.FILE_UNKNOWN or WPN.FILE_404):
        logs.critical("Weapon hash is either unknown or has an error")
        logs.critical(hashData)
        return({"error": hashData})
    return({
        "fileTarget": hashData[0],
        "fileStruct": hashData[1],
        "fileVersion": hashData[2]
    })


@app.get("/weapon/backup")
async def weaponBackup(
    rootDirectory: str = Query(...),
    fileType: str = Query(...),
    fileTarget: str = Query(...),
):
    # Check if arguments are correct
    # FILE TYPE
    conditions = [WPN.FILE_TYPE_1P, WPN.FILE_TYPE_3P, WPN.FILE_TYPE_HP, WPN.FILE_TYPE_MP]
    if fileType not in conditions:
        errorMsg = "Given file type is unknown"
        logs.critical("Internal API error: /weapon/backup")
        logs.critical(errorMsg)
        logs.critical(fileType)
        return {"error": errorMsg}
    # FILE TARGET
    fileTarget = fileTarget.upper()
    if fileTarget not in attr_wpnList():
        errorMsg = "Given file target is unknown"
        logs.critical("Internal API error: /weapon/hashmdl")
        logs.critical(errorMsg)
        logs.critical(fileTarget)
        return {"error": errorMsg}

    r = wpn_backupMDL(rootDirectory, fileType, fileTarget)
    return {"result": r}


@app.get("/weapon/installskin")
async def weaponInstallSkin(
    materialDir: str = Query(...),
    weaponName: str = Query(...),
    skinID: str = Query(...),
):
    # XXX Will only delete the materials used by the target skin. Will not remove other
    # materials if they are not in the desired skin.
    filePath = r"{0}\{1}\{2}".format(DATA.WEAPON_SKIN, weaponName, skinID)
    fileInfoPath = r"{0}\{1}".format(filePath, DATA.FILE_JSON_INFO)
    infoAPI = getWeaponSkinInfo(weaponName, skinID)
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
        elif Path(fileInfoPath).is_file():
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
        # XXX TODO use the makedirs func if server is ok and not downloaded bfore
        # os.makedirs(filePath)  # Create all the required dirs
    # return(json.loads(result.text))
