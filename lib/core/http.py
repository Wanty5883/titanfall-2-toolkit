# TPL - Third Party Libraries
import requests
# LPL - Local Python Libraries
from lib.core.enums import NETWORK
from lib.core.log import logger as logs


def requestsGET(url, query, timeout=None):
    headers = {"user-agent": NETWORK.USER_AGENT}
    try:
        result = requests.get(url=url, params=query, headers=headers, timeout=timeout)
        return(result)
    except requests.exceptions.ConnectionError as error:
        # logs.error(format(requests.exceptions.ConnectionError))
        # logs.error(format(error))
        return{"error": 503}
    except requests.exceptions.Timeout as error:
        # logs.error(format(requests.exceptions.Timeout))
        # logs.error(format(error))
        return{"error": 504}


def getWeaponSkinInfo(weaponName, skinID):
    url = "{0}/r2/weapon/skin".format(NETWORK.URL_API)
    query = {"weaponName": weaponName, "skinID": skinID}
    result = requestsGET(url, query)
    return(result)
