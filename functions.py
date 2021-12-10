import time
import pyautogui as pyAG
import pydirectinput as pyDI

from get_window import *
from check_functions import *
from config import key_bindings

def time_stamp(self):
    t = time.localtime()
    current_time = time.strftime('%H:%M', t)
    print("\n//", current_time, "LOOP#", self, "//")
    time.sleep(0.25)

# Prints casts left to the next repair function
def casts_left_to_repair(casts_repair, casts_count):
    if (casts_repair - casts_count != 0):
        print('[INFO] Casts until next repair: ', (casts_repair - casts_count))

# Change to "fishing stance"
def enter_fishing_stance():
    pyDI.press((key_bindings.FISHING_MODE))
    time.sleep(1.25)

# Casts the fishing pole
def cast_fishing(self):
    time.sleep(0.25)
    pyDI.mouseDown(button='left')
    time.sleep(self)
    pyDI.mouseUp(button='left')

# Waits until a fish is caught
def catch_fish():
    while check_lure_onscreen():
        continue
    pyDI.mouseDown()

    for i in range(10):
        if check_reel_on_screen():
            print('[OK] FISH CAUGHT')
            break
    
    if not check_reel_on_screen():
        print('[ERROR] UNSUCCESSFUL ATTEMPT')

# Pickups the reel
def pick_up_reel():
    while True:
        pyDI.keyDown((key_bindings.FREE_LOOK))
        f3_shown = pyAG.locateOnScreen('images/f3_fishing.png', region=(650, 450, int(screen_width/2), int(screen_height/2)), confidence = 0.9, grayscale = True)
        max_reel = pyAG.locateOnScreen('images/max_reel.png', confidence = 0.9, grayscale = True)

        if f3_shown != None:
            pyDI.keyUp((key_bindings.FREE_LOOK))
            time.sleep(0.5)
            break
        elif check_reel_on_screen() == False:
            pyDI.click()
            time.sleep(0.5)
            continue
        elif max_reel != None:
            pyDI.mouseDown()
            continue
        elif max_reel == None:
            pyDI.mouseUp()
            time.sleep(0.5)
            continue

# Repair the fishing pole
def repair():
    time.sleep(0.5)
    pyDI.press(key_bindings.INVENTORY)
    time.sleep(0.5)
    position = pyAG.locateCenterOnScreen('images/f3_inventory.png', confidence = 0.7, grayscale = True)

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
        print('[ERROR] Fishing pole not detected (?)')

# Sets a bait
def set_bait():
    if check_bait():
        try:
            pyDI.press(key_bindings.EQUIP_BAIT)
            bait_pos = pyAG.locateCenterOnScreen('images/esc_bait_menu.png', confidence = 0.7, grayscale = True)
            time.sleep(0.5)
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
            print('[ERROR] Cannot attach a bait (?), will try again on the next loop.')
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
    print('[INFO] Group rejected.')
    time.sleep(0.75)