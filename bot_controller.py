#zatím slouží k veškerému inputu který budeme potřebovat
import pyautogui
import mouse
import time


def press(key):
    pyautogui.press(key)

def get_cursor_pos():
    return mouse.get_position()

def set_cursor_pos(x,y):
    mouse.move(x,y)

def click(x,y):
    set_cursor_pos(x,y)
    wait(0.1)
    mouse.click('left')
    
def wait(t):
    time.sleep(t)