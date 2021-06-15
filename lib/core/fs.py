# SPL - Standard Python Libraries
import ntpath
import os
import shutil
# LPL - Local Python Libraries
from lib.core.enums import NETWORK
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
