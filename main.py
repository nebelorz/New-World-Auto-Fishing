import hotkeys
from functions import *
from reconnect import *
from get_window import *
from check_functions import *
from config import Settings

## VARIABLES
loop_count = 1
repair_count = 0
chests_count = 0

if check_window('New World'):
    get_window('New World')
    cursor_to_screen()

    while True:
        if hotkeys.event_pause.is_set():
            print('[HOTKEY] PROGRAM PAUSED')
            hotkeys.event_resume.wait()
            get_window('New World')
            cursor_to_screen()

        elif Settings.RECONNECT and check_disconnection():
            reconnect()

        elif Settings.LOOPS_TO_REPAIR == repair_count:
            repair()
            repair_count = 0

        elif check_afk():
            anti_afk()

        elif Settings.REJECT_GROUP and check_group_invite():
            reject_group()

        else:
            loop_stamp(loop_count, chests_count)

            if not check_start():
                enter_fishing_stance()

            if Settings.SET_BAIT and check_no_bait_attached():
                set_bait()

            if check_start():
                cast_fishing(Settings.CAST_STRENGTH)
                        
                if check_lure_landed():
                    catch_fish()
                    pick_up_reel()
                    if check_treasure_chest():
                        chests_count += 1
                    
                    loop_count += 1
                    repair_count += 1
                    loops_to_repair(Settings.LOOPS_TO_REPAIR, repair_count)
                    continue