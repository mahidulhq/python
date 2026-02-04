import time
import pyautogui

def screenshot():
    name = int(round(time.time() * 1000))
    name = '/home/panda/Documents/python_learning/python/project01/screenshotData/{}.png'.format(name)
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()
    
screenshot()