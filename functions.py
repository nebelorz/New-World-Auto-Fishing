import time
import pyautogui as pyAG
import pydirectinput as pyDI

from get_window import *
from check_functions import *
from config import KeyBindings
from reconnect import check_disconnection


def loop_stamp(loop, tchests):
    # Prints TIME, LOOP number and TREASURE CHESTS count
    t = time.localtime()
    current_time = time.strftime('%H:%M', t)
    
    print("\n// [" + current_time + "]", "LOOP #" + str(loop), "||", "T-CHESTS: " + str(tchests), "\\\\")
    time.sleep(0.25)

def loops_to_repair(loops_repair, loop_count):
    # Prints loops left to call the next repair function
    if (loops_repair - loop_count) != 0:
        print('[INFO] LOOPS UNTIL NEXT REPAIR:', (loops_repair - loop_count))

def enter_fishing_stance():
    pyDI.press((KeyBindings.FISHING_MODE))
    time.sleep(1.25)

def cast_fishing(self):
    pyDI.mouseDown()
    time.sleep(self)
    pyDI.mouseUp()

def catch_fish(): # Waits until a fish bites the hook
    if check_lure_onscreen():
        for i in range(400):
            if check_lure_onscreen():
                continue
            else:
                break
    pyDI.mouseDown()
    time.sleep(0.25)

    for i in range(20):
        if check_reel_on_screen():
            print('[OK] FISH HOOKED')
            break
    
    if not check_reel_on_screen():
        print('[ERROR] UNSUCCESSFUL ATTEMPT')

def pick_up_reel():
    pyDI.keyDown((KeyBindings.FREE_LOOK))
    for i in range(20):      
        if check_start() is not None:
            break

        elif not check_reel_on_screen():
            pyDI.click()
            time.sleep(0.25)
            continue

        elif check_disconnection() is not None:
            break

        elif check_reel_on_screen():
            for i in range(20):
                can_reel = pyAG.locateOnScreen('images/can_reel.png', confidence = 0.9, grayscale = True)
                if can_reel is not None:
                    pyDI.mouseDown()
                    continue
                if can_reel is None:
                    pyDI.mouseUp()
                    break
        continue
    
    pyDI.keyUp((KeyBindings.FREE_LOOK))

def repair(): # Repairs the fishing pole
    time.sleep(0.5)
    pyDI.press(KeyBindings.INVENTORY)
    time.sleep(0.5)
    position = pyAG.locateCenterOnScreen('images/f3_inventory.png', region=(650, 500, int(screen_width/4), int(screen_height/4)), confidence = 0.7, grayscale = True)

    if position is not None:
        pyDI.moveTo((position[0] - 50), position[1]) # Mouse to rod slot
        time.sleep(0.75)
        pyDI.keyDown((KeyBindings.REPAIR))
        pyDI.click()
        pyDI.keyUp((KeyBindings.REPAIR))
        time.sleep(0.5)
        pyDI.press((KeyBindings.INTERACT))
        time.sleep(0.5)
        pyDI.press((KeyBindings.INVENTORY))
        time.sleep(0.5)
        print('[OK] FISHING POLE REPAIRED')
    else:
        print('[ERROR] FISHING POLE NOT DETECTED (?)')

def set_bait():
    if check_no_bait_attached():
        try:
            pyDI.press(KeyBindings.EQUIP_BAIT)
            time.sleep(0.5)
            bait_pos = pyAG.locateCenterOnScreen('images/esc_bait_menu.png', region=(900, 0, int(screen_width/2), screen_height), confidence = 0.7, grayscale = True)
            time.sleep(0.5)
            pyDI.moveTo(int(bait_pos[0]) + 10, int(bait_pos[1]) + 210)
            time.sleep(0.5)
            pyDI.click()
            time.sleep(0.25)
            check_baits_left() # If 0 baits left, function is not called anymore
            pyDI.moveTo(int(bait_pos[0]) + 330, int(bait_pos[1]) + 580)
            time.sleep(0.25)
            pyDI.click()
            time.sleep(2.50)
            if Settings.SET_BAIT:
                print('[OK] BAIT ATTACHED')
        except:
            print('[ERROR] CANNOT ATTACH A BAIT (?), WILL TRY AGAIN ON THE NEXT LOOP')
            time.sleep(1)

def anti_afk():
    time.sleep(0.25)
    pyDI.keyDown(KeyBindings.MOVE_LEFT)
    time.sleep(0.10)
    pyDI.keyUp(KeyBindings.MOVE_LEFT)
    time.sleep(0.10)
    pyDI.keyDown(KeyBindings.MOVE_RIGHT)
    time.sleep(0.10)
    pyDI.keyUp(KeyBindings.MOVE_RIGHT)
    time.sleep(0.5)

def reject_group():
    pyDI.press(KeyBindings.REJECT_GROUP)
    print('[INFO] GROUP REJECTED')
    time.sleep(0.75)