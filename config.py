import random


####################
# GENERAL SETTINGS #
####################
class settings():
    CAST_STRENGTH = random.uniform(1.7, 1.9)    # (1.9, 1.9) to always land MAX)
    CASTS_TO_REPAIR = 60                        # Casts until the fishing rod is repaired

    SET_BAIT = None     # None -- Will skip attaching a bait
                        # True -- Will attach a bait everytime it expires

################
# KEY BINDINGS #
################
class key_bindings():
    JUMP         = 'space'
    CHAT         = 'enter'
    REPAIR       = 'r'
    INTERACT     = 'e'
    EQUIP_BAIT   = 'r'
    FREE_LOOK    = 'alt'
    INVENTORY    = 'tab'
    FISHING_MODE = 'f3'