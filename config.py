import random


# # # # # # # # # # # # # # # # # # #
#  G E N E R A L   S E T T I N G S  #
# # # # # # # # # # # # # # # # # # #
class Settings():
    CAST_STRENGTH = random.uniform(1.7, 1.9) # (1.9, 1.9) to always land MAX)
    LOOPS_TO_REPAIR = 300                    # Loops until the fishing rod is repaired

    SET_BAIT = True         # True  -- Will attach a bait everytime it expires
                            # False -- Skips attaching baits
                            
    REJECT_GROUP = True     # True  -- Auto reject group invites
                            # False -- Skips rejecting group invites

    # FUNCTION IN BETA
    RECONNECT = True        # True  -- Reconnects when disconnection is detected
                            # False -- Skips reconnection attempts



# # # # # # # # # # # # # # #
#  K E Y  B I N D I N G S   #
# # # # # # # # # # # # # # #
class KeyBindings():
    REPAIR       = 'r'
    INTERACT     = 'e'
    MOVE_LEFT    = 'a'
    MOVE_RIGHT   = 'd'
    FREE_LOOK    = 'alt'
    INVENTORY    = 'tab'
    EQUIP_BAIT   = 'r'
    REJECT_GROUP = 'f2' # Cannot be changed
    FISHING_MODE = 'f3' # Cannot be changed

    # HOTKEYS (resume/pause)
    RESUME_KEY = 'home'
    PAUSE_KEY  = 'end'
