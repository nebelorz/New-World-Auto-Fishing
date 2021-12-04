import time
import pyautogui as pyAG

# Checks if the fishing pole is drawn, if not, pulls it out
def check_drawn_pole():
    drawn_pole = pyAG.locateOnScreen('images/f3_fishing.png', confidence = 0.7, grayscale = True)
    if drawn_pole == None:
        return(False)
    else:
        return(True)

# Checks for the fishing bubble
def check_cast_fishing():
    while True:
        time.sleep(3.5)
        fishing_casted = pyAG.locateOnScreen('images/fishing_casted.png', confidence = 0.7, grayscale = True)
        for i in range(3):
            if fishing_casted == None:
                print('... waiting to land the line #{}'.format(i))
                time.sleep(1.5)
                continue
            else:
                print('[OK] LURE CAST FOUND')
                return(True)
        break

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