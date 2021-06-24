# TPL - Third Party Libraries
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Query
from typing import Optional
# LPL - Local Python Libraries
import lib.r2.wpn_enums as WPN_ENUMS
from lib.core.attr import attr_wpnList
from lib.core.enums import SETTING
from lib.core.enums import WPN
from lib.core.fs import fs_readConfigFileVPK
from lib.core.fs import fs_writeConfigFileVPK
from lib.core.log import logger_api as logs
from lib.r2.wpn import wpn_backupMDL
from lib.r2.wpn import wpn_convertMDL
from lib.r2.wpn import wpn_hashMDL
from lib.r2.wpn import wpn_installSkin


app = FastAPI()
# APP = app


@app.get("/settings/vpk")
async def settings(
    settingsMode: str = Query(...),
    vpkTarget: Optional[str] = None,
    vpkPath: Optional[str] = None,
):
    vpkList = [
        None,
        SETTING.VPK_COMMON,
        SETTING.VPK_FRONTEND,
        SETTING.VPK_MP_AC,
        SETTING.VPK_MP_BWC,
        SETTING.VPK_MP_BOO,
        SETTING.VPK_MP_CC,
        SETTING.VPK_MP_CP,
        SETTING.VPK_MP_COL,
        SETTING.VPK_MP_COM,
        SETTING.VPK_MP_CRA,
        SETTING.VPK_MP_DEC,
        SETTING.VPK_MP_DRY,
        SETTING.VPK_MP_EDE,
        SETTING.VPK_MP_EXO,
        SETTING.VPK_MP_FOR,
        SETTING.VPK_MP_GLI,
        SETTING.VPK_MP_MEA,
        SETTING.VPK_MP_REL,
        SETTING.VPK_MP_RIS,
        SETTING.VPK_MP_STA,
        SETTING.VPK_MP_TOW,
        SETTING.VPK_MP_TRA,
        SETTING.VPK_MP_UMA,
        SETTING.VPK_MP_WAR,
    ]
    if vpkTarget not in vpkList:
        raise HTTPException(status_code=400, detail="vpkTarget is incorrect")
    if settingsMode in (SETTING.MODE_READ, SETTING.MODE_READALL):
        result = fs_readConfigFileVPK(settingsMode, vpkTarget)
        return(result)
    elif settingsMode == SETTING.MODE_WRITE:
        result = fs_writeConfigFileVPK(vpkTarget, vpkPath)
        return


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
    result = wpn_convertMDL(rootDirectory, fileType, fileVersion, fileTarget.upper(), structTarget.upper())
    return {"result": result}


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

    result = wpn_backupMDL(rootDirectory, fileType, fileTarget)
    return {"result": result}


@app.get("/weapon/installskin")
async def weaponInstallSkin(
    materialDir: str = Query(...),
    weaponName: str = Query(...),
    skinID: str = Query(...),
):
    """
    Do the different operation in order to install a weapon custom skin
    """
    result = wpn_installSkin(materialDir, weaponName, skinID)
    return(result)
