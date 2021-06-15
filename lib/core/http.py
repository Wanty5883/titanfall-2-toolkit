# TPL - Third Party Libraries
import requests
# LPL - Local Python Libraries
from lib.core.enums import NETWORK


def requestsGET(url, query, timeout=None):
    headers = {"user-agent": NETWORK.USER_AGENT}
    r = requests.get(url=url, params=query, headers=headers, timeout=timeout)
    return(r)


def getWeaponSkinInfo(weaponName, skinID):
    url = "{0}/r2/weapon/skin".format(NETWORK.URL_API)
    query = {"weaponName": weaponName, "skinID": skinID}
    r = requestsGET(url, query)
    return(r)
