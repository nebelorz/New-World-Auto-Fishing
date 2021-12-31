import subprocess
import win32gui
import win32con


subprocess.Popen('cmd')

hwnd = win32gui.GetForegroundWindow()

win32gui.MoveWindow(hwnd, 0, 0, 500, 250, True)
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 500, 250, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)


subprocess.call('cls', shell=True)
subprocess.call('python .\main.py', shell=True)