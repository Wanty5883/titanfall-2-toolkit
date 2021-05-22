# SPL - Standard Python Libraries
from inspect import isclass
# LPL - Local Python Libraries
import lib.core.enums as ENUMS
import lib.r2.wpn_enums as ENUMS_WPN


def attr_wpnList():
    """
    Make a list of classes in 'wpn_enums.py'. Each weapons has its own class.
    """
    enums_classes = [x for x in dir(ENUMS) if isclass(getattr(ENUMS, x))]
    wpn_classes = [x for x in dir(ENUMS_WPN) if isclass(getattr(ENUMS_WPN, x))]
    # Negate "enums.py" classes from wpn_classes
    wpn_enums = [x for x in wpn_classes if x not in enums_classes]
    return(wpn_enums)
