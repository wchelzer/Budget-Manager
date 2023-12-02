# Author: Wyatt Helzer
# Creation Date: 12/1/2023
# Date Last Updated: 12/1/2023
# Function: ...

#---------------------------------------------------------------------------------------------

import tkinter
import mysql.connector

from tkinter import messagebox
from tkinter import Toplevel
from tkinter import filedialog



class BudgetGUI:

    def __init__(self):
        self.main = tkinter.Tk()
        self.main_frame = tkinter.Frame(self.main)
        
        # main screen buttons
        self.login_button = tkinter.Button(self.main_frame, text="LOGIN", command = self.login_frame)
        self.register_button = tkinter.Button(self.main_frame, text="REGISTER", command = self.register)
        self.no_register_button = tkinter.Button(self.main_frame, text="CONTINUE WITHOUT\n REGISTERING", command = self.register) # change the command for this button
        
        self.login_button.pack(side="top")
        self.register_button.pack(side="bottom")
        self.no_register_button.pack(side="bottom")

        self.main_frame.pack()



        tkinter.mainloop()
        
        
    def login_frame(self):
        # print("Login")
        self.login_screen = Toplevel(self.main)
        self.login_screen.title("Login Page")

        


    def register(self):
        print("Register")





if __name__ == "__main__":
    
    # Creates database connection
    db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Mr_Kaboom1939")
    
    BudgetGUI()