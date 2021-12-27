import time
import pyautogui as pyAG
import pygetwindow as pyGW

screen_width, screen_height = pyAG.size() # Screen dimmensions

def cursor_to_screen():
    pyAG.moveTo(screen_width/2, screen_height/3)

def check_window(self):
    try:
        pyGW.getWindowsWithTitle(self)[0]
        return(True)
    except:
        print(self, 'not found')
        return(False)
        
def get_window(self):
    window = pyGW.getWindowsWithTitle(self)[0]
    if window.isMinimized:
        window.restore()
        window.activate()
        window.maximize()
        time.sleep(0.5)
    else:
        window.activate()
        window.maximize()
        time.sleep(0.5)

def minimize_window(self):
    window = pyGW.getWindowsWithTitle(self)[0]
    window.minimize()