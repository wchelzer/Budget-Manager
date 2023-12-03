# Author: Wyatt Helzer
# Creation Date: 12/1/2023
# Date Last Updated: 12/2/2023
# Function: ...

#---------------------------------------------------------------------------------------------

import tkinter
import mysql.connector

from tkinter import messagebox
from tkinter import Toplevel
from tkinter import filedialog


if __name__ == "__main__":
    
    # Creates database connection
    db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Mr_Kaboom1939")
    
    # Creates main menu
    main = tkinter.Tk()
    main.title("Budget Manager")
    



    def register_frame():
        global register_username
        global register_password
        global register_password_verification
        
        register_screen = Toplevel(main)
        register_screen.title("Register Page")

        register_username = tkinter.StringVar()
        register_password = tkinter.StringVar()
        register_password_verification = tkinter.StringVar()

        # labels
        register_info_label = tkinter.Label(register_screen, text="Enter new login information")
        register_username_label = tkinter.Label(register_screen, text="Username")
        register_password_label = tkinter.Label(register_screen, text="Password")
        register_password_verification_label = tkinter.Label(register_screen, text="Confirm your password")

        # entries
        register_username_entry = tkinter.Entry(register_screen, textvariable=register_username)
        register_password_entry = tkinter.Entry(register_screen, textvariable=register_password, show="*")
        register_password_verification_entry = tkinter.Entry(register_screen, textvariable=register_password_verification, show="*")

        # button
        register_button = tkinter.Button(register_screen, text="REGISTER", command=filler)

        # grid
        register_info_label.grid(row=0, column=0, columnspan=2)
        register_username_label.grid(row=1, column=0)
        register_username_entry.grid(row=1, column=1)
        register_password_label.grid(row=2, column=0)
        register_password_entry.grid(row=2, column=1)
        register_password_verification_label.grid(row=3, column=0)
        register_password_verification_entry.grid(row=3, column=1)
        register_button.grid(row=4, column=1)





    def login_frame():
        # print("Login")
        login_screen = Toplevel(main)
        login_screen.title("Login Page")


    def filler():
        print("You clicked me!")



    # main screen info
    username = tkinter.StringVar()
    password = tkinter.StringVar()
    
    login_button = tkinter.Button(main, text="LOGIN", command = login_frame)
    register_button = tkinter.Button(main, text="REGISTER", command = register_frame)
    continue_button = tkinter.Button(main, text="CONTINUE WITHOUT\n REGISTERING", command = register_frame) # change the command for this button
    username_label = tkinter.Label(main, text="Username")
    password_label = tkinter.Label(main, text="Password")
    username_entry = tkinter.Entry(main, textvariable=username)
    password_entry = tkinter.Entry(main, textvariable=password, show="*")
    
    username_label.grid(row=0, column=0)
    username_entry.grid(row=0, column=1)
    password_label.grid(row=1, column=0)
    password_entry.grid(row=1, column=1)
    login_button.grid(row=0, column=2, rowspan=2)
    register_button.grid(row=2, column=0)
    continue_button.grid(row=2, column=1)
    
    
    tkinter.mainloop()
    