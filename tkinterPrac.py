#import Tkinter as tk
from Tkinter import *
from tkFileDialog import *
import tkMessageBox


class mikesButtons:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        
        self.printButton = Button(frame, text = "step1", command = self.printMessage)
        self.printButton.pack(side=LEFT)
        
        self.runButton = Button(frame, text = "run", command = self.callback)
        self.runButton.pack(side=LEFT)
        
        self.quitButton = Button(frame, text = "Quit", command = frame.quit)
        self.quitButton.pack(side=LEFT)
        
    def printMessage(self):
        print("Choose a photo")
    
    def callback(self):
        execfile("project.py")

root = Tk()

root.wm_title("Image To Sound")

fileName = askopenfilename(parent=root)

b = mikesButtons(root)


root.geometry("600x550+200+200")
root.mainloop()















"""
def photo1():
    photo1 = PhotoImage(file = "1.png")
    label1 = Label(topFrame, image = photo1)
    label1.pack(side = LEFT)
def photo2():
    photo2 = PhotoImage(file = "1.png")
    label2 = Label(topFrame, image = photo2)
    label2.pack(side = LEFT)
def photo3():
    photo3 = PhotoImage(file = "1.png")
    label3 = Label(bottomFrame, image = photo3)
    label3.pack(side = LEFT)
"""
"""
class Application(tk.Frame):

    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
    
    def createWidgets(self):
        self.runButton = tk.Button(self, text ='Run', command = self.quit)
        self.runButton.grid()
    
    def createWidgets(self):
        self.quitButton = tk.Button(self, text ='Quit', command = self.quit, padx = 20)
        self.quitButton.grid()
    

app = Application()
app.master.title('Sample application')
app.mainloop()


********************************

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)

button1 = Button(topFrame, text = "Button 1", fg = "red")
button2 = Button(topFrame, text = "Button 2", fg = "blue")
button3 = Button(topFrame, text = "Button 3", fg = "green")
button4 = Button(bottomFrame, text = "Button 4", fg = "purple")

button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)
button4.pack(side = LEFT)

************************************

one = Label(root, text = "one", bg = "red", fg = "white")
one.pack()
two = Label(root, text = "two", bg = "green", fg = "green")
two.pack(fill=X)
three = Label(root, text = "three", bg = "blue", fg = "white")
three.pack(side = LEFT, fill=Y)

************************************

label1 = Label(root, text = "Name")
label2 = Label(root, text = "Password")
entry1 = Entry(root)
entry2 = Entry(root)
label1.grid(row = 0, sticky = E)
label2.grid(row = 1, sticky = E)

entry1.grid(row = 0,column = 1)
entry2.grid(row = 1,column = 1)

c = Checkbutton(root, text = "Keep me signed in")
c.grid(columnspan = 2)

***************************

def printName():
    print("Hello World")
    
button1 = Button(root, text = "say hello", command = printName)
button1.pack()


*****************************

def leftClick(event):
    print("Left")

def middleClick(event):
    print("Middle")

def rightClick(event):
    print("Right")

frame = Frame(root, width = 300, height =  250)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)

frame.pack()


********************************
class mikesButtons:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        
        self.printButton = Button(frame, text = "Print Message", command = self.printMessage)
        self.printButton.pack(side=LEFT)
        
        self.quitButton = Button(frame, text = "Quit", command = frame.quit)
        self.quitButton.pack(side=LEFT)
        
    def printMessage(self):
        print("It worked!!")


root = Tk()
b = mikesButtons(root)
root.mainloop()


toolbar = Frame(root) 

insertButt = Button(toolbar, text = "Insert image", command = doNothing).pack(side = LEFT, padx = 2, pady = 2) 
printButt = Button(toolbar, text = "Print", command = doNothing).pack(side = LEFT, padx = 2, pady = 2) 
toolbar.pack(side = TOP, fill = X) 
"""
