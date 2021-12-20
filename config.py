import random


####################
# GENERAL SETTINGS #
####################
class settings():
    CAST_STRENGTH = random.uniform(1.7, 1.9)    # (1.9, 1.9) to always land MAX)
    LOOPS_TO_REPAIR = 10                        # Loops until the fishing rod is repaired

    SET_BAIT = False     # True  -- Will attach a bait everytime it expires
                         # False -- Skips attaching baits
    
    RECONNECT = True     # True  -- Reconnects when disconnection is detetced
                         # False -- Skips reconnection attempts
                        
    REJECT_GROUP = False    # True  -- Auto reject group invites
                            # False -- Skips rejecting group invites

################
# KEY BINDINGS #
################
class key_bindings():
    REPAIR       = 'r'
    INTERACT     = 'e'
    MOVE_LEFT    = 'a'
    MOVE_RIGHT   = 'd'
    FREE_LOOK    = 'alt'
    INVENTORY    = 'tab'
    EQUIP_BAIT   = 'r'
    REJECT_GROUP = 'f2' # Cannot be changed
    FISHING_MODE = 'f3' # Cannot be changed