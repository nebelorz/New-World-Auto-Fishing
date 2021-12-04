import time
import pyautogui as pyAG
import pydirectinput as pyDI

from config import key_bindings

# Checks if the fishing pole is drawn, if not, pulls it out
def check_drawn_pole():
    drawn_pole = pyAG.locateOnScreen('images/f3_fishing.png', confidence = 0.7, grayscale = True)
    if drawn_pole == None:
        pyDI.press((key_bindings.FISHING_MODE))
        time.sleep(1.5)

# Checks for the fishing bubble
def check_cast_fishing():
    while True:
        fishing_casted = pyAG.locateOnScreen('images/fishing_casted.png', confidence = 0.7, grayscale = True)
        if fishing_casted == None:
            continue
        else:
            print('[OK] BUBBLE CAST FOUND')
            return(True)

# Checks if a bait is attached
def check_bait():
    no_bait = pyAG.locateCenterOnScreen('images/no_bait.png', confidence = 0.7, grayscale = True)
    if no_bait != None:
        return(True)
    else:
        return(False)

# Checks for the anti-AFK message
def check_afk():
    afk_detection = pyAG.locateCenterOnScreen('images/afk_detection.png', confidence = 0.7, grayscale = True)
    if afk_detection != None:
        return(True)
    else:
        return(False)