import pyautogui as pyAG
import pydirectinput as pyDI

from get_window import *

## CONSTANTS
STEP_1_NAME = 'ok_button'
STEP_1_NUM = 1

STEP_2_NAME = 'continue_button'
STEP_2_NUM = 2

STEP_3_NAME = 'play_button'
STEP_3_NUM = 3

STEP_FINAL_NAME = 'connected'


def check_disconnection():
    check_step_1 = pyAG.locateOnScreen('images/reconnect/{}.png'.format(STEP_1_NAME), confidence = 0.7, grayscale = True)
    check_step_2 = pyAG.locateOnScreen('images/reconnect/{}.png'.format(STEP_2_NAME), confidence = 0.7, grayscale = True)
    check_step_3 = pyAG.locateOnScreen('images/reconnect/{}.png'.format(STEP_3_NAME), confidence = 0.7, grayscale = True)

    if check_step_1 or check_step_2 or check_step_3 is not None:
        return(True)

def check_disconnection_step(self):
    disconnected = pyAG.locateOnScreen('images/reconnect/{}.png'.format(self), confidence = 0.8, grayscale = True)
    if disconnected is not None:
        return(True)

def disconnection_step(self): # Clicks on designed step button
    button = pyAG.locateCenterOnScreen('images/reconnect/{}.png'.format(self), confidence = 0.7, grayscale = True)
    pyDI.moveTo(int(button[0]), int(button[1]))
    pyDI.click()

def wait_next_step(self):
    if not check_disconnection_step('{}'.format(self)):
        time.sleep(1)

def reconnect():
    print('-[ DISCONNECTION DETECTED ]-')
    while True:
        try:
            if check_disconnection_step(STEP_1_NAME):
                print('... RECONNECTION IN PROGRESS ({}/3) ...'.format(STEP_1_NUM))
                while check_disconnection_step(STEP_1_NAME):
                    disconnection_step(STEP_1_NAME)
                    wait_next_step(STEP_2_NAME)
            
            elif check_disconnection_step(STEP_2_NAME):
                print('... RECONNECTION IN PROGRESS ({}/3) ...'.format(STEP_2_NUM))
                while check_disconnection_step(STEP_2_NAME):
                    disconnection_step(STEP_2_NAME)
                    wait_next_step(STEP_3_NAME)
            
            elif check_disconnection_step(STEP_3_NAME):
                print('... RECONNECTION IN PROGRESS ({}/3) ...'.format(STEP_3_NUM))
                while check_disconnection_step(STEP_3_NAME):
                    disconnection_step(STEP_3_NAME)
                    wait_next_step(STEP_FINAL_NAME)
            
            elif check_disconnection_step(STEP_FINAL_NAME):
                print('-[ RECONNECTED SUCCESFULLY ]-')
                break
            else:
                continue
        except:
            break