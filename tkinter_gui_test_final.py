#Importing Pythons GUI library
from tkinter import *

#Setting up the GUI
root = Tk()
root.title("Simple GUI") #GUI window title
root.geometry("520x200") #GUI window size

myLabel4 = Label(root)


#Creating an input box
myInput1 = Entry(root, width=50, borderwidth=5)
myInput1.insert(0, "Enter A Text Here") #Predefine an input

#Creating a function that is executed when clicking the button
def myClick():
    global myLabel4
    myLabel4.destroy()  #Delete the old label text before adding a new one 
    
    myLabel3 = Label(root, text="You have succesfully clicked the button!").grid(row=4, column=1)

    Output = "Your input was: " + myInput1.get()
    myLabel4 = Label(root, text=Output)   #Output the input with button click
    myLabel4.grid(row=5, column=1)

#Creating a label widget
#   'padx' and 'pady' for button size, 'command=' for running the function, 'fg=' for forground color, 'bg=' for background color
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="This is a GUI Programm.")
myButton1 = Button(root, text="This is a Button.", padx=50, pady=30, command=myClick, fg="red", bg="black", borderwidth=5)

#Showing it onto the screen   
#  .grid(row=0, column=0) for position .pack() for none          
myLabel1.grid(row=0, column=0) 
myLabel2.grid(row=0, column=2)
myButton1.grid(row=3, column=1)
myInput1.grid(row=2, column=1)

#Making the programm main loop until closed
root.mainloop()

