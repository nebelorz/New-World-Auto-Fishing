import time
import pyautogui as pyAG
import pydirectinput as pyDI

# Checks if the fishing pole is drawn, if not, pulls it out
def check_drawn_pole():
    drawn_pole = pyAG.locateOnScreen('images/f3_fishing.png', confidence = 0.7, grayscale = True)
    if drawn_pole == None:
        pyDI.press('f3')
        time.sleep(1.5)

# Checks for the fishing bubble
def check_cast_fishing():
    time.sleep(5)
    fishing_casted = pyAG.locateOnScreen('images/fishing_casted.png', confidence = 0.7, grayscale = True)
    if fishing_casted == None:
        print('No bubble cast found on screen.')
        return(False)
    else:
        print('Bubble cast found')
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