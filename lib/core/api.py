# SPL - Standard Python Libraries
from inspect import isclass
# TPL - Third Party Libraries
import uvicorn
from fastapi import FastAPI
from fastapi import Query
# LPL - Local Python Libraries
from lib.core.attr import attr_wpnList
from lib.core.enums import API
from lib.core.enums import WPN
from lib.core.log import logger_api as logs
from lib.r2.wpn import wpn_hashMDL
from lib.r2.wpn import wpn_convertMDL
import lib.r2.wpn_enums as WPN_ENUMS


app = FastAPI()
APP = app


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
    return {r: True}


# TODO find a better way to do this
# XXX JS py-shell library ?
# XXX Or JS using a uvicorn command by itself ? Is that even doable ?
# if __name__ == "lib.core.api":
#     uvicorn.run(app, port=API.SERVER_PORT)
