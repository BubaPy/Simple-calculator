#author: BubaPy
#author 2: Omar-M-Z

import tkinter as tk
from tkinter import *

class Application():
    def __init__(self, master):
        #creating the window, setting the dimensions, and centering the window on the screen
        self.master = master
        master.title("New Year CountDown")
        window_width = 300
        window_height = 400
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        master.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.add_widgets()

    def add_widgets(self):
        #stuff like buttons will be added here
        pass

root = Tk()
root.resizable(False, False)
application = Application(root)
root.mainloop()