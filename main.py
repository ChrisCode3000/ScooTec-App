#Importing the used librarys
from tkinter import *           #GUI Library
import sqlite3                  #Database Library

#GUI Settings
root = Tk() #Creating the main GUI window
root.title('ScooTec Rentals')   #Setting the window title
root.iconbitmap('Scooter.ico')  #Setting the window icon
root.geometry("165x220")        #Setting the window size

#Global variables / label widgets that are necesary 
L7 = Label(root)
L8 = Label(root)
L9 = Label(root)
L10 = Label(root)
query_label = Label(root)

#Creating functions that are executed when clicking the buttons
def pricef(distance):
    distance = float(distance)
    price = str(round(0.99+0.18*distance,2))
    return price

def register(): #inception of this file (database.py)
    exec(open("./database.py").read(), globals())

def C1(): #C1 = New Window Function
    global T1
    T1 = Toplevel(root)     #Open a new window
    T1.title('Rent A Scooter')
    T1.iconbitmap('Scooter.ico')

    def C3(): #C3 = Calculating and printing the rental details   
        #Calling Global Variables
        global L7, L8, L9, L10 
        #Clearing the Labels before filling them with new values
        L7.destroy()       
        L8.destroy()
        L9.destroy()         
        L10.destroy()

        #Calculating the Price (0.99€ unlockfee + 0.18€ per km)
        #Converting from string to float and back to string, rounding to 2 decimal places
        distance = float(I4.get())
        price = str(round(0.99+0.18*distance, 2))
      
        #Creating label widgets that show the rental details
        L6 = Label(T1, text="Rental Details:")
        L7 = Label(T1, text="User ID: " + I2.get())
        L8 = Label(T1, text="Name:")
        L9 = Label(T1, text="Distance: " + I4.get() + " km")
        L10 = Label(T1, text="Price: " + price + " €")
        L11 = Label(T1, text="(0.99€ unlockfee + 0.18€ per km)")
        L12 = Label(T1, text="")

        #Printing them onto the screen
        L6.grid(row=6, column=0, columnspan=2)
        L7.grid(row=7, column=0, columnspan=2)
        L8.grid(row=8, column=0, columnspan=2)
        L9.grid(row=9, column=0, columnspan=2)
        L10.grid(row=10, column=0, columnspan=2)
        L11.grid(row=11, column=0, columnspan=2)
        L12.grid(row=12, column=0, columnspan=2)
    
    # Create Query Function for searching the User by User ID
    def query():
        #Calling Global Variables
        global query_label
        #Clearing the Labels before filling them with new values
        query_label.destroy()

        # Create a database or connect to one
        conn = sqlite3.connect('scootec_data.db')
        # Create cursor
        c = conn.cursor()

        # Query the database for the user id
        user_id = int(I2.get())
        c.execute("SELECT * FROM users WHERE oid=?", (user_id,))
        records = c.fetchmany(1)
        print(records)

        # Loop Thru Results
        print_records = ''
        for record in records:
            print_records += str(record[0]) + " " + str(record[1]) + " "

        query_label = Label(T1, text="Name: " + print_records)
        query_label.grid(row=8, column=0, columnspan=2)

        #Commit Changes
        conn.commit()

        # Close Connection 
        conn.close()
    

    #Creating label widgets in the "rent a scooter" process window (T1)
    L1 = Label(T1, text="Start your scooter rental here:")
    L2 = Label(T1, text="User ID:")
    I2 = Entry(T1, width=10, borderwidth=5)
    L3 = Label(T1, text="Scooter ID:")
    I3 = Entry(T1, width=10, borderwidth=5)
    L4 = Label(T1, text="Rental Distance: (km)")
    I4 = Entry(T1, width=10, borderwidth=5)
    L5 = Label(T1, text="")
    B1 = Button(T1, text="start", command=lambda:[C3(),query()])
    L13 = Label(T1, text="Don't have an User ID yet?")
    B13 = Button(T1, text="register now", command=register) 
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
    L13.grid(row=13, column=0)
    B13.grid(row=13, column=1)
    B0.grid(row=14, column=0, columnspan=2) 
     
#Creating label widgets in main window (root)
#   'padx' and 'pady' for button size, 'command=' for running the function, 'fg=' for forground color, 'bg=' for background color
L1 = Label(root, text="Welcome at ScooTec Rentals!")
L2 = Label(root, text="What would you like to do?")
B1 = Button(root, text="rent a scooter", padx=40, pady=20, command=C1, fg="black", bg="white", borderwidth=5)
B2 = Button(root, text="register", command=register, padx=40, pady=20, fg="black", bg="white", borderwidth=5)
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