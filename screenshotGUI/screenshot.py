import time
import pyautogui
import tkinter

def screenshot():
    name = int(round(time.time() * 1000))
    name = '/home/panda/Documents/python_learning/screenshotGUI/screenshotData/{}.png'.format(name)
    # time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()
    

# tkinter ->
root = tkinter.Tk()
frame = tkinter.Frame(root)
frame.pack()

button = tkinter.Button(
    frame,
    text="Capture Screenshot",
    command=screenshot)

button.pack(side=tkinter.LEFT)
close = tkinter.Button(
    frame,
    text="QUIT",
    command=quit)
close.pack(side=tkinter.LEFT)

root.mainloop()

