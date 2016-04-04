#import Tkinter as tk
from Tkinter import *
from tkFileDialog import *
import tkMessageBox
from PIL import ImageTk, Image
import math
import pyaudio



class mikesButtons:
    global image
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        
        self.runButton = Button(frame, text = "run", command = self.callback)
        self.runButton.pack(side=LEFT)
        
        self.quitButton = Button(frame, text = "Quit", command = frame.quit)
        self.quitButton.pack(side=LEFT)
    
    def callback(self):
        execfile("project.py")
root = Tk()

root.wm_title("Image To Sound")

fileName = askopenfilename(parent=root)


b = mikesButtons(root)


root.geometry("600x550+200+200")
root.mainloop()



