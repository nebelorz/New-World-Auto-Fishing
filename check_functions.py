import time
import pyautogui as pyAG
import pydirectinput as pyDI

from get_window import *
from config import Settings


def check_start(): # Checks F3 on screen to start the loop
    start = pyAG.locateOnScreen('images/f3_fishing.png', region=(650, 450, int(screen_width/2), int(screen_height/2)), confidence = 0.7, grayscale = True)
    if start is not None:
        return(True)

def check_no_bait_attached():
    no_bait = pyAG.locateOnScreen('images/no_bait_equipped.png', region=(900, 0, int(screen_width/2), screen_height), confidence = 0.7, grayscale = True)
    if no_bait is not None:
        return(True)

def check_baits_left():
    no_baits_left = pyAG.locateOnScreen('images/no_baits_left.png', region=(900, 0, int(screen_width/2), screen_height), confidence = 0.9, grayscale = True)
    if no_baits_left is not None:
        Settings.SET_BAIT = False
        print('[INFO] NO BAITS LEFT - BAITS WILL NO LONGER BE ATTACHED')

def check_lure_landed():
    time.sleep(3)
    for i in range(3):
        if not check_lure_onscreen():
            print('... waiting to land the line ...')
            time.sleep(1.5)
            continue
        else:
            print('[OK] LURE FOUND')
            return(True)

    print('[INFO] RESTARTING THE LOOP (LURE NOT FOUND)')
    pyDI.click(button='right')
    time.sleep(1.75)

def check_lure_onscreen():
    lure = pyAG.locateOnScreen('images/lure.png', confidence = 0.7, grayscale = True)
    if lure is not None:
        return(True)

def check_reel_on_screen():
    reel_on_screen = pyAG.locateOnScreen('images/reel_on_screen.png', confidence = 0.8, grayscale = True)
    if reel_on_screen is not None:
        return(True)

def check_afk(): # Checks for the AFK message at top RIGHT
    afk_detection = pyAG.locateOnScreen('images/afk_detection.png', region=(0, 0, int(screen_width), int(screen_height/3)), confidence = 0.85, grayscale = True)
    if afk_detection is not None:
        return(True)

def check_group_invite():
    group_invite = pyAG.locateOnScreen('images/f2_reject.png', region=(0, 0, int(screen_width), int(screen_height/3)), confidence = 0.7, grayscale = True)
    if group_invite is not None:
        return(True)

def check_treasure_chest(): # Checks for a fished treasure chest
    treasure_chest = pyAG.locateOnScreen('images/treasure_chest.png', region=(650, 450, int(screen_width/2), int(screen_height/2)), confidence = 0.7, grayscale = True)
    if treasure_chest is not None:
        return(True)