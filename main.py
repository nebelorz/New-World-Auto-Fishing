import random
from functions import *
from check_functions import *
from get_window import *

## VARS ##
# CAST
CAST_TIME = random.uniform(1.7, 1.9)    #cast with random strength (1.9 for MAX)

# REPAIR
REPAIR_COUNT = 0
CASTS_TO_REPAIR = 60    #casts until the fishing rod is repaired

# BAIT (None or True)
SET_BAIT = None


if check_window('New World') == True:
    get_window('New World')

    while True:
        time_stamp()
        check_drawn_pole()
        if REPAIR_COUNT >= CASTS_TO_REPAIR:
            repair()
            REPAIR_COUNT = 0
        elif check_afk() == False:
            anti_afk()
        else:
            if SET_BAIT == True and check_bait() == True:
                try:
                    set_bait()
                except:
                    SET_BAIT == None
                    print("[ERROR] Bait not found")
            
            cast_fishing(CAST_TIME)

            if check_cast_fishing() == True:
                catch_fish()
                pick_up_reel()
                print('Casts until next repair: ', (CASTS_TO_REPAIR - REPAIR_COUNT))
                REPAIR_COUNT += 1
                continue
            else:
                continue