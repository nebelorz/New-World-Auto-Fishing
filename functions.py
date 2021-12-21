import time
import pyautogui as pyAG
import pydirectinput as pyDI

from get_window import *
from check_functions import *
from config import key_bindings
from reconnect import check_disconnection


def loop_stamp(loop, tchests):
    t = time.localtime()
    current_time = time.strftime('%H:%M', t)
    
    #prints TIME, LOOPnumber and TREASURE CHESTScount
    print("\n// [" + current_time + "]", "LOOP #" + str(loop), "||", "T-CHESTS: " + str(tchests), "\\\\")
    time.sleep(0.25)

# Prints casts left to the next repair function
def loops_to_repair(loops_repair, loop_count):
    if (loops_repair - loop_count) != 0:
        print('[INFO] LOOPS UNTIL NEXT REPAIR:', (loops_repair - loop_count))

# Enter "fishing stance"
def enter_fishing_stance():
    pyDI.press((key_bindings.FISHING_MODE))
    time.sleep(1.25)

# Casts the fishing pole
def cast_fishing(self):
    pyDI.mouseDown()
    time.sleep(self)
    pyDI.mouseUp()

# Waits until a fish bites the hook
def catch_fish():
    while check_lure_onscreen():
        continue
    pyDI.mouseDown()

    for i in range(10):
        if check_reel_on_screen():
            print('[OK] FISH HOOKED')
            break
    
    if not check_reel_on_screen():
        print('[ERROR] UNSUCCESSFUL ATTEMPT')

# Pickups the reel
def pick_up_reel():
    pyDI.keyDown((key_bindings.FREE_LOOK))
    while not check_disconnection():        
        if check_start() != None:
            break
        elif not check_reel_on_screen():
            pyDI.click()
            time.sleep(0.25)
            continue

        while check_reel_on_screen():
            can_reel = pyAG.locateOnScreen('images/can_reel.png', confidence = 0.9, grayscale = True)
            if can_reel != None:
                pyDI.mouseDown()
                continue
            if can_reel == None:
                pyDI.mouseUp()
                break
        continue
    
    pyDI.keyUp((key_bindings.FREE_LOOK))

# Repair the fishing pole
def repair():
    time.sleep(0.5)
    pyDI.press(key_bindings.INVENTORY)
    time.sleep(1)
    position = pyAG.locateCenterOnScreen('images/f3_inventory.png', region=(650, 500, int(screen_width/4), int(screen_height/4)), confidence = 0.7, grayscale = True)

    if position != None:
        pyDI.moveTo((position[0] - 50), position[1]) #mouse to rod slot
        time.sleep(1)
        pyDI.keyDown((key_bindings.REPAIR))
        pyDI.click()
        pyDI.keyUp((key_bindings.REPAIR))
        time.sleep(1)
        pyDI.press((key_bindings.INTERACT))
        pyDI.press((key_bindings.INVENTORY))
        time.sleep(1)
        print('[OK] FISHING POLE REPAIRED')
    else:
        print('[ERROR] FISHING POLE NOT DETECTED (?)')

# Sets a bait
def set_bait():
    if check_bait():
        try:
            pyDI.press(key_bindings.EQUIP_BAIT)
            time.sleep(0.5)
            bait_pos = pyAG.locateCenterOnScreen('images/esc_bait_menu.png', region=(900, 0, int(screen_width/2), screen_height), confidence = 0.7, grayscale = True)
            time.sleep(1.5)
            pyDI.moveTo(int(bait_pos[0]) + 10, int(bait_pos[1]) + 210)
            time.sleep(0.5)
            pyDI.click()
            time.sleep(0.25)
            check_baits_left()
            pyDI.moveTo(int(bait_pos[0]) + 330, int(bait_pos[1]) + 580)
            time.sleep(0.25)
            pyDI.click()
            time.sleep(2.50)
            if settings.SET_BAIT:
                print('[OK] BAIT ATTACHED')
        except:
            print('[ERROR] CANNOT ATTACH A BAIT (?), WILL TRY AGAIN ON THE NEXT LOOP.')
            time.sleep(1)

# Anti AFK
def anti_afk():
    time.sleep(0.25)
    pyDI.keyDown(key_bindings.MOVE_LEFT)
    time.sleep(0.10)
    pyDI.keyUp(key_bindings.MOVE_LEFT)
    time.sleep(0.10)
    pyDI.keyDown(key_bindings.MOVE_RIGHT)
    time.sleep(0.10)
    pyDI.keyUp(key_bindings.MOVE_RIGHT)
    time.sleep(0.5)

# Reject group invite
def reject_group():
    pyDI.press(key_bindings.REJECT_GROUP)
    print('[INFO] GROUP REJECTED.')
    time.sleep(0.75)