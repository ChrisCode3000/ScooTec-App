#Importing Pythons GUI library
from tkinter import *

#Setting up the GUI
root = Tk()

#Creating a label widget
myLabel = Label(root, text="Hello World!")

#Showing it onto the screen
myLabel.pack()

#Making the programm main loop until closed
root.mainloop()

