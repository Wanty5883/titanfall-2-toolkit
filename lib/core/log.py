# SPL - Standard Python Libraries
import logging
from logging.handlers import TimedRotatingFileHandler
import os
import sys


def getLogger(loggerName):
    loggerDir = "logs"
    loggerFile = "{0}\\log".format(loggerDir)

    # Create log folder if it does not exist
    if not os.path.exists(loggerDir):
        os.makedirs(loggerDir)

    # 00:00:42 | WPN | [INFO] | Done super secret modding method
    loggingFormatter = logging.Formatter(
        "%(asctime)s | [%(levelname)s] | %(message)s",
        "%H:%M:%S"
    )

    consoleHandler = logging.StreamHandler(sys.stdout)
    consoleHandler.setFormatter(loggingFormatter)
    fileHandler = TimedRotatingFileHandler(loggerFile, when="midnight")
    fileHandler.setFormatter(loggingFormatter)

    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(consoleHandler)
    logger.addHandler(fileHandler)
    logger.propagate = False
    return(logger)


logger = getLogger("CLIENT")
logger_api = getLogger("API")
