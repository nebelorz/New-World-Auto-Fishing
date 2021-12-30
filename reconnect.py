import pyautogui as pyAG
import pydirectinput as pyDI

from get_window import *

## CONSTANTS
REFRESH_BUTTON = 'refresh'

STEP_1_NAME = 'ok_button'
STEP_1_NUM = 1

STEP_2_NAME = 'continue_button'
STEP_2_NUM = 2

STEP_3_NAME = 'play_button'
STEP_3_NUM = 3


STEP_FINAL_NAME = 'connected'


def check_disconnection():
    step_1 = pyAG.locateOnScreen('images/reconnect/{}.png'.format(STEP_1_NAME), confidence = 0.7, grayscale = True)
    step_2 = pyAG.locateOnScreen('images/reconnect/{}.png'.format(STEP_2_NAME), confidence = 0.7, grayscale = True)
    step_3 = pyAG.locateOnScreen('images/reconnect/{}.png'.format(STEP_3_NAME), confidence = 0.7, grayscale = True)

    if step_1 or step_2 or step_3 is not None:
        return(True)

def check_step(self):
    disconnected = pyAG.locateOnScreen('images/reconnect/{}.png'.format(self), confidence = 0.8, grayscale = True)
    if disconnected is not None:
        return(True)

def disconnection_step(self): # Clicks on the actual step button
    button = pyAG.locateCenterOnScreen('images/reconnect/{}.png'.format(self), confidence = 0.7, grayscale = True)
    pyDI.moveTo(int(button[0]), int(button[1]))
    pyDI.click()

def wait_for_step(self):
    if self is STEP_FINAL_NAME:
        loops = 60 # Waiting for final step up to a minute
    else:
        loops = 10

    for i in range(loops):
        if not check_step('{}'.format(self)):
            time.sleep(1)
            continue
        else:
            break

def reconnect():
    print('-[ DISCONNECTION DETECTED ]-')
    while check_disconnection():
        try:

            if check_step(STEP_1_NAME):
                print('... RECONNECTION IN PROGRESS ({}/3) ...'.format(STEP_1_NUM))
                disconnection_step(STEP_1_NAME)
                wait_for_step(STEP_2_NAME)
            
            elif check_step(STEP_2_NAME):
                print('... RECONNECTION IN PROGRESS ({}/3) ...'.format(STEP_2_NUM))
                disconnection_step(STEP_2_NAME)
                wait_for_step(STEP_3_NAME)
            
            elif check_step(STEP_3_NAME):
                print('... RECONNECTION IN PROGRESS ({}/3) ...'.format(STEP_3_NUM))
                disconnection_step(REFRESH_BUTTON)
                time.sleep(4)
                disconnection_step(STEP_3_NAME)
                wait_for_step(STEP_FINAL_NAME)

                if check_step(STEP_FINAL_NAME):
                    print('-[ RECONNECTED SUCCESFULLY ]-')

            else:
                continue

        except:
            break