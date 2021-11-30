import time
import pyautogui as pyAG
import pydirectinput as pyDI

def time_stamp():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)

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
            pyDI.click()
            print('[OK] FISH CAUGHT')
            break

# Pickups the reel
def pick_up_reel():
    while True:
        pyDI.keyDown('alt')
        reel_on_screen = pyAG.locateOnScreen('images/reel_on_screen.png', confidence = 0.9, grayscale = True)
        max_reel = pyAG.locateOnScreen('images/max_reel.png', confidence = 0.9, grayscale = True)
        stop = pyAG.locateOnScreen('images/f3_fishing.png', confidence = 0.9, grayscale = True)
        
        if stop != None:
            time.sleep(0.25)
            pyDI.keyUp('alt')
            time.sleep(0.50)
            break
        elif reel_on_screen == None:
            pyDI.click()
            continue
        elif max_reel != None:
            pyDI.mouseDown()
            continue
        elif max_reel == None:
            pyDI.mouseUp()
            time.sleep(1)
            continue

# Repair the fishing pole
def repair():
    time.sleep(0.5)
    pyDI.press('tab')
    time.sleep(0.5)
    position = pyAG.locateCenterOnScreen('images/f3_inventory.png', confidence = 0.7, grayscale = True)

    if position != None:
        pyDI.moveTo((position[0] - 50), position[1]) #mouse to rod slot
        time.sleep(1)
        pyDI.keyDown('r')
        pyDI.click()
        pyDI.keyUp('r')
        time.sleep(1)
        pyDI.press('e')
        pyDI.press('tab')
        time.sleep(1)
        print('[OK] FISHING POLE REPAIRED')
    else:
        print('Fishing pole not detected (?)')

# Sets a bait
def set_bait():
    no_bait = pyAG.locateCenterOnScreen('images/no_bait.png', confidence = 0.7, grayscale = True)
    if no_bait != None:
        pyDI.press('r')
        time.sleep(0.5)
        bait_pos = pyAG.locateCenterOnScreen('images/esc_bait_menu.png', confidence = 0.7, grayscale = True)

        pyDI.moveTo((bait_pos[0]) + 10, bait_pos[1] + 210)
        time.sleep(0.25)
        pyDI.click()
        time.sleep(0.25)
        pyDI.moveTo((bait_pos[0] + 330), bait_pos[1] + 580)
        time.sleep(0.5)
        pyDI.click()
        time.sleep(2.50)
        print('[OK] BAIT ATTACHED')

# Anti AFK
def anti_afk():
    pyDI.press('enter')
    time.sleep(0.25)
    pyAG.write('/sit')
    time.sleep(0.25)
    pyDI.press('enter')
    time.sleep(1.5)
    pyDI.press('space')
    time.sleep(0.5)