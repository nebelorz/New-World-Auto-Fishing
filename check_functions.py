import time
import pyautogui as pyAG
import pydirectinput as pyDI

from get_window import *
from config import settings

# Checks if the fishing pole is drawn, if not, pulls it out
def check_drawn_pole():
    drawn_pole = pyAG.locateOnScreen('images/f3_fishing.png', confidence = 0.7, grayscale = True)
    if drawn_pole != None:
        return(True)

# Checks lure on screen
def check_lure_onscreen():
    lure = pyAG.locateOnScreen('images/lure.png', confidence = 0.7, grayscale = True)
    if lure != None:
        return(True)
    else:
        return(False)

# Checks reel on screen
def check_reel_on_screen():
    reel_on_screen = pyAG.locateOnScreen('images/reel_on_screen.png', confidence = 0.8, grayscale = True)
    if reel_on_screen != None:
        return(True)
    else:
        return(False)

# Checks landing the lure
def check_lure_landed():
    time.sleep(4)
    while True:
        for i in range(3):
            if check_lure_onscreen() == False:
                print('... waiting to land the line ...')
                time.sleep(1.5)
                continue
            else:
                print('[OK] LURE CAST FOUND')
                return(True)

        print('[INFO] RESTARTING THE LOOP (LURE NOT FOUND)')
        pyDI.click(button='right')
        time.sleep(1.75)
        break

# Checks if a bait is attached
def check_bait():
    no_bait = pyAG.locateOnScreen('images/no_bait_equipped.png', confidence = 0.8, grayscale = True)
    if no_bait != None:
        return(True)

def check_baits_left():
    no_baits_left = pyAG.locateOnScreen('images/no_baits_left.png', region=(750, 500, int(screen_width/2), int(screen_height/2)), confidence = 0.9, grayscale = True)
    if no_baits_left != None:
        settings.SET_BAIT = False
        print('[INFO] NO BAITS LEFT - BAITS WILL NO LONGER BE ATTACHED')

# Checks for the AFK message
def check_afk():
    afk_detection = pyAG.locateOnScreen('images/afk_detection.png', confidence = 0.7, grayscale = True)
    if afk_detection != None:
        return(True)
    else:
        return(False)

# Checks group invite
def check_group_invite():
    group_invite = pyAG.locateOnScreen('images/f2_reject.png', confidence = 0.7, grayscale = True)
    if group_invite != None:
        return(True)