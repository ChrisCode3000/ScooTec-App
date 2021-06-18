#Importing the used librarys
from tkinter import *           #GUI Library
from PIL import ImageTk,Image   #Image Library
import sqlite3                  #Database Library


root = Tk() #Creating the main GUI window
root.title('ScooTec Rentals')   #Setting the window title
root.iconbitmap('Scooter.ico')  #Setting the window icon
root.geometry("165x220")        #Setting the window size

#Creating functions that are executed when clicking the buttons
def C1():
    T1 = Toplevel(root)     #Open a new window
	#T1.title('Rent A Scooter')
	#T1.iconbitmap('Scooter.ico')
    
   
    #Creating label widgets in the new window
    L1 = Label(T1, text="Start your scooter rental here:")
    L2 = Label(T1, text="User ID:")
    I2 = Entry(T1, width=10, borderwidth=5)
    L3 = Label(T1, text="Scooter ID:")
    I3 = Entry(T1, width=10, borderwidth=5)
    L4 = Label(T1, text="Rental Distance:")
    I4 = Entry(T1, width=10, borderwidth=5)
    L5 = Label(T1, text="")
    L6 = Label(T1, text="Rental Details:")
    L7 = Label(T1, text="User ID: ")
    L8 = Label(T1, text="Name:")
    L9 = Label(T1, text="Distance:")
    L10 = Label(T1, text="Price:")
    L11 = Label(T1, text="")
    B1 = Button(T1, text="start")
    
    L12 = Label(T1, text="Don't have an User ID yet?")
    B12 = Button(T1, text="register now") 
    B0 = Button(T1, text="close window", command=T1.destroy)

    #Showing the label widgets in the new window
    L1.grid(row=0, column=0, columnspan=2) 
    L2.grid(row=1, column=0)
    I2.grid(row=1, column=1)  
    L3.grid(row=2, column=0)
    I3.grid(row=2, column=1)  
    L4.grid(row=3, column=0)
    I4.grid(row=3, column=1)  
    B1.grid(row=4, column=0, columnspan=2) 
    L5.grid(row=5, column=0)
    L6.grid(row=6, column=0, columnspan=2)
    L7.grid(row=7, column=0)
    L8.grid(row=8, column=0)
    L9.grid(row=9, column=0)
    L10.grid(row=10, column=0)
    L11.grid(row=11, column=0)
    L12.grid(row=12, column=0)
    B12.grid(row=12, column=1)
    B0.grid(row=13, column=0, columnspan=2) 
    
    


def C2():
    T2 = Toplevel()
	#T2.title('Rent A Scooter')
	#T2.iconbitmap('Scooter.ico')
    B2 = Button(T2, text="close window", command=T2.destroy).pack()

#Creating label widgets
#   'padx' and 'pady' for button size, 'command=' for running the function, 'fg=' for forground color, 'bg=' for background color
L1 = Label(root, text="Welcome at ScooTec Rentals!")
L2 = Label(root, text="What would you like to do?")
B1 = Button(root, text="rent a scooter", padx=40, pady=20, command=C1, fg="black", bg="white", borderwidth=5)
B2 = Button(root, text="register", padx=40, pady=20, command=C2, fg="black", bg="white", borderwidth=5)
B3 = Button(root, text="close window", command=root.destroy, bg="white", borderwidth=5)

#Showing them onto the screen   
#  .grid(row=0, column=0) for position .pack() for none          
L1.grid(row=0, column=0) 
L2.grid(row=1, column=0) 
B1.grid(row=2, column=0) 
B2.grid(row=3, column=0) 
B3.grid(row=4, column=0) 

#Making the programm main loop until closed
root.mainloop()