from functions import *
from reconnect import *
from get_window import *
from check_functions import *
from config import settings

## VARIABLES
LOOP_COUNT = 1
REPAIR_COUNT = 0
TCHESTS_COUNT = 0

PAUSED = False

if check_window('New World'):
    get_window('New World')
    cursor_to_screen()

    while True:
        if check_disconnection() and settings.RECONNECT:
            reconnect()

        elif REPAIR_COUNT == settings.LOOPS_TO_REPAIR:
            repair()
            REPAIR_COUNT = 0

        #elif check_afk():
            #anti_afk()

        elif check_group_invite() and settings.REJECT_GROUP:
            reject_group()

        else:
            loop_stamp(LOOP_COUNT, TCHESTS_COUNT)

            if not check_start():
                enter_fishing_stance()

            if settings.SET_BAIT and check_bait():
                set_bait()

            if check_start():
                cast_fishing(settings.CAST_STRENGTH)
                        
                if check_lure_landed():
                    catch_fish()
                    pick_up_reel()
                    if check_treasure_chest():
                        TCHESTS_COUNT += 1
                    
                    LOOP_COUNT += 1
                    REPAIR_COUNT += 1
                    loops_to_repair(settings.LOOPS_TO_REPAIR, REPAIR_COUNT)
                    continue