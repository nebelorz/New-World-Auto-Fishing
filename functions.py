import time
import pyautogui as pyAG
import pydirectinput as pyDI

from config import key_bindings

def time_stamp(self):
    t = time.localtime()
    current_time = time.strftime('%H:%M', t)
    print("\n//", current_time, "LOOP#", self, "//")
    time.sleep(0.25)

def casts_left_to_repair(casts_repair, casts_count):
    if (casts_repair - casts_count != 0):
        print('[INFO] Casts until next repair: ', (casts_repair - casts_count))

def cursor_to_center():
    screenWidth, screenHeight = pyAG.size()
    pyAG.moveTo(screenWidth/2, screenHeight/2)

# Change to "fishing stance"
def enter_fishing_stance():
    pyDI.press((key_bindings.FISHING_MODE))
    time.sleep(1.25)

# Casts the fishing pole
def cast_fishing(self):
    pyDI.mouseDown(button='left')
    time.sleep(self)
    pyDI.mouseUp(button='left')

# Waits until a fish is caught
def catch_fish():
    while True:
        fish_caught = pyAG.locateOnScreen('images/fish_caught.png', confidence = 0.9, grayscale = True)
        if fish_caught == None:
            continue
        else:
            pyDI.click(button='left')
            print('[OK] FISH CAUGHT')
            break

# Pickups the reel
def pick_up_reel():
    while True:
        pyDI.keyDown((key_bindings.FREE_LOOK))
        reel_on_screen = pyAG.locateOnScreen('images/reel_on_screen.png', confidence = 0.8, grayscale = True)
        max_reel = pyAG.locateOnScreen('images/max_reel.png', confidence = 0.9, grayscale = True)
        stop = pyAG.locateOnScreen('images/f3_fishing.png', confidence = 0.9, grayscale = True)
        
        if stop != None:
            pyDI.keyUp((key_bindings.FREE_LOOK))
            time.sleep(0.75)
            break
        elif reel_on_screen == None:
            pyDI.click()
            time.sleep(0.25)
            continue
        elif max_reel != None:
            pyDI.mouseDown()
            continue
        elif max_reel == None:
            pyDI.mouseUp()
            time.sleep(0.50)
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
    no_bait = pyAG.locateCenterOnScreen('images/no_bait.png', confidence = 0.7, grayscale = True)
    try:
        if no_bait != None:
            pyDI.press((key_bindings.EQUIP_BAIT))
            time.sleep(0.5)
            bait_pos = pyAG.locateCenterOnScreen('images/esc_bait_menu.png', confidence = 0.7, grayscale = True)
            time.sleep(0.25)
            pyDI.moveTo((bait_pos[0]) + 10, bait_pos[1] + 210)
            time.sleep(0.25)
            pyDI.click()
            time.sleep(0.25)
            pyDI.moveTo((bait_pos[0] + 330), bait_pos[1] + 580)
            time.sleep(0.5)
            pyDI.click()
            time.sleep(2.50)
            print('[OK] BAIT ATTACHED')
    except:
        print('[ERROR] Cannot attach a bait (?), will try again on the next loop.')

# Anti AFK
def anti_afk():
    time.sleep(0.25)
    pyDI.press(key_bindings.MOVE_LEFT)
    pyDI.press((key_bindings.MOVE_RIGHT))
    time.sleep(0.25)