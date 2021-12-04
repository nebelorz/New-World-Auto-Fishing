from functions import *
from get_window import *
from check_functions import *
from config import settings


## CONSTANTS
LOOP_COUNT = 1
REPAIR_COUNT = 0

if check_window('New World') == True:
    get_window('New World')
    cursor_to_center()

    while True:
        if REPAIR_COUNT == settings.CASTS_TO_REPAIR:
            repair()
            REPAIR_COUNT = 0
        elif check_afk() == True:
            anti_afk()
        else:
            time_stamp(LOOP_COUNT)
            check_drawn_pole()
            if settings.SET_BAIT == True and check_bait() == True:
                set_bait()
        
            cast_fishing(settings.CAST_STRENGTH)
            
            if check_cast_fishing() == True:
                catch_fish()
                pick_up_reel()
                
                REPAIR_COUNT += 1
                LOOP_COUNT += 1
                casts_left_to_repair(settings.CASTS_TO_REPAIR, REPAIR_COUNT)
                continue
            else:
                continue