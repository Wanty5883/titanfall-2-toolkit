# TPL - Third Party Libraries
import uvicorn
from fastapi import FastAPI
# LPL - Local Python Libraries
from lib.core.attr import attr_wpnList
from lib.core.enums import API
from lib.core.enums import WPN
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




# TODO find a better way to do this
# XXX JS py-shell library ?
# XXX Or JS using a uvicorn command by itself ? Is that even doable ?
# if __name__ == "lib.core.api":
#     uvicorn.run(app, port=API.SERVER_PORT)
