from threading import Event
from keyboard import add_hotkey

from config import KeyBindings



event_pause = Event()
event_resume = Event()

def pause(): # Sets event_pause and clears event_resume
    if not event_pause.is_set():
        print('[HOTKEY] PROGRAM PAUSED ON THE NEXT LOOP')
    event_pause.set()
    event_resume.clear()

def resume(): # Sets event_resume and clears event_pause
    if not event_resume.is_set() and event_pause.is_set():
        print('[HOTKEY] PROGRAM RESUMED')
    event_resume.set()
    event_pause.clear()



add_hotkey(KeyBindings.PAUSE_KEY, pause)    # Add hotkeys
add_hotkey(KeyBindings.RESUME_KEY, resume)