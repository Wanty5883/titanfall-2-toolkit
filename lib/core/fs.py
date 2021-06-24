# SPL - Standard Python Libraries
import json
import ntpath
import os
import shutil
# LPL - Local Python Libraries
from lib.core.enums import DATA
from lib.core.enums import NETWORK
from lib.core.enums import SETTING
from lib.core.log import logger as logs


def fs_backupFile(originalPath):
    """
    Just a small function to backup a file in the same folder
    adding "backup_" in the name of the file too
    """
    logs.info("Making backup of {0}".format(originalPath))
    if not os.path.isfile(originalPath):  # Check if the file does not exist
        logs.critical("File not found")
        return(NETWORK.MESSAGE_ERROR)
    # TODO move "backup_" in enums, but find a suited class
    fileFolder, fileName = ntpath.split(originalPath)
    targetName = "backup_{0}".format(fileName)
    targetPath = "{0}\{1}".format(fileFolder, targetName)
    shutil.copyfile(originalPath, targetPath)
    return(NETWORK.MESSAGE_SUCCESS)


def fs_readConfigFileVPK(settingsMode, vpkTarget):
    if settingsMode == SETTING.MODE_READALL:
        with open(DATA.CONFIG_FILE, "r") as file:
            return(json.load(file)["vpk"])
    if settingsMode == SETTING.MODE_READ:
        with open(DATA.CONFIG_FILE, "r") as file:
            return(json.load(file)["vpk"][vpkTarget])


def fs_writeConfigFileVPK(vpkTarget, vpkPath):
    with open(DATA.CONFIG_FILE, "w+") as file:
        configData = json.load(file)
        configData["vpk"][vpkTarget] = vpkPath
        file.seek(0)
        json.dump(configData, file)
        file.truncate()

    return
