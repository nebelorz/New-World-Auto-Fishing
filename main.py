from functions import *
from get_window import *
from check_functions import *
from config import settings


## CONSTANTS
LOOP_COUNT = 1
REPAIR_COUNT = 0

if check_window('New World'):
    get_window('New World')
    cursor_to_center()

    while True:
        if REPAIR_COUNT == settings.CASTS_TO_REPAIR:
            repair()
            REPAIR_COUNT = 0
        elif check_afk():
            anti_afk()
        elif check_group_invite() and settings.REJECT_GROUP:
            reject_group()
        else:
            time_stamp(LOOP_COUNT)

            if not check_drawn_pole():
                enter_fishing_stance()

            if settings.SET_BAIT and check_bait():
                set_bait()

            if check_drawn_pole():
                cast_fishing(settings.CAST_STRENGTH)
                        
                if check_lure_landed():
                    catch_fish()
                    pick_up_reel()
                    
                    REPAIR_COUNT += 1
                    LOOP_COUNT += 1
                    casts_left_to_repair(settings.CASTS_TO_REPAIR, REPAIR_COUNT)
                    continue