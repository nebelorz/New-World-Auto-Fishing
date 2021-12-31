import pyautogui as pyAG

screen_width, screen_height = pyAG.size() # Screen dimmensions

def cursor_to_screen():
    pyAG.moveTo(screen_width/2, screen_height/3)

def check_window(self):
    try:
        pyAG.getWindowsWithTitle(self)[0]
        return(True)
    except:
        print(self, 'not found')
        return(False)

def get_window(self):
    window = pyAG.getWindowsWithTitle(self)[0]

    if window.isMinimized:
        window.activate()
        window.maximize()
    else:
        window.activate()