#Importing Pythons GUI library
from tkinter import *

#Setting up the GUI
root = Tk()

#Creating a function that is executed when clicking the button
def myClick():
    myLabel = Label(root, text="You have succesfully clicked the button!").grid(row=3, column=1)

#Creating a label widget
#   'padx' and 'pady' for button size, 'command=' for running the function
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="This is a GUI Programm.")
myButton1 = Button(root, text="This is a Button.", padx=50, pady=30, command=myClick)

#Showing it onto the screen   
#  .grid(row=0, column=0) for position .pack() for none          

myLabel1.grid(row=0, column=0) 
myLabel2.grid(row=0, column=2)
myButton1.grid(row=2, column=1)

#Making the programm main loop until closed
root.mainloop()

