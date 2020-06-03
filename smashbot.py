import pyautogui as pygui
import pygetwindow as gw
from directkeys import PressKey, ReleaseKey, W, A, S, D

# More DirectInput keyboard scan codes at: https://gist.github.com/tracend/912308
RIGHT = 0xCD
top, left, bottom, right = 0,0,0,0

def keyDown(x):
    return PressKey(x)

def keyUp(x):
    return ReleaseKey(x)


def click():
    return pygui.click()


def moveTo(x, y):
    return pygui.moveTo(x, y)


def setup():
    global left, top, right, bottom
    window = gw.getAllTitles()
    for title in window:
        if "Super" in title:
            window = title
    window = gw.getWindowsWithTitle(window)[0]
    window.moveTo(5, 5)
    window.resizeTo(600, 500)
    left, top = window.topleft
    right, bottom = window.bottomright


def main():
    setup()
    moveTo(10,10)
    click()
    for i in range(5):
        keyDown(RIGHT)
    keyUp(RIGHT)



main()
