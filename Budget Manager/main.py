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
    password = "Mr_Kaboom1939",
    database = "budget_manager")
    
    # Creates main menu
    main = tkinter.Tk()
    main.title("Budget Manager")
    


    def complete_registration():
        username = register_username.get()
        password = register_password.get()
        password_verification = register_password_verification.get()


        if(username == "" or password == "" or password_verification == ""):
            print("All fields are required")
            return
        elif(password != password_verification):
            print("Your password must be the same in both fields")
            return
        else:
            # print("Registration successful!")
            cursor = db.cursor()
            cursor.execute("SELECT username, password FROM user")
            accounts = cursor.fetchall()
            
            # if there are no accounts in the database
            if(len(accounts) == 0):
                query = "INSERT INTO user(username, password) VALUES(%s, %s)"
                value = (username, password)
                cursor.execute(query, value)
                db.commit()
                print("Registration successful!")
                return

            for i in range(len(accounts)):
                print(accounts[i][0], accounts[i][1])
                if(username == accounts[i][0] or password == accounts[i][1]):
                    print("Username or password already exists")
                    return
            else:
                query = "INSERT INTO user(username, password) VALUES(%s, %s)"
                value = (username, password)
                cursor.execute(query, value)
                db.commit()
                print("Registration successful!")
                return



    def register_frame():
        global register_username
        global register_password
        global register_password_verification
        
        register_screen = Toplevel(main)
        register_screen.title("Registration Page")

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
        register_button = tkinter.Button(register_screen, text="REGISTER", command=complete_registration)

        # grid
        register_info_label.grid(row=0, column=0, columnspan=2)
        register_username_label.grid(row=1, column=0)
        register_username_entry.grid(row=1, column=1)
        register_password_label.grid(row=2, column=0)
        register_password_entry.grid(row=2, column=1)
        register_password_verification_label.grid(row=3, column=0)
        register_password_verification_entry.grid(row=3, column=1)
        register_button.grid(row=4, column=1)




    def complete_login():
        if(username.get() == "" or password.get() == ""):
            print("All fields are required")
            return
        else:
            cursor = db.cursor()
            cursor.execute("SELECT username, password FROM user")
            accounts = cursor.fetchall()

            for i in range(len(accounts)):
                if(accounts[i][0] == username.get() and accounts[i][1] == password.get()):
                    print("Login successful!")
                    budget_board()
                    return
            else:
                print("Account doesn't exist. Please check your information or register an account")
                return
        
        

    def budget_board():
        budget_frame = tkinter.Toplevel(main)
        budget_frame.title("Budget Manager")

        global monthly_expenses
        global monthly_income
        global budget_duration
        global monthly_wants
        global monthly_savings

        monthly_expenses = tkinter.StringVar()
        monthly_income = tkinter.StringVar()
        budget_duration = tkinter.IntVar()
        monthly_wants = tkinter.DoubleVar()
        monthly_savings = tkinter.DoubleVar()

        # labels
        monthly_expenses_label = tkinter.Label(budget_frame, text="Enter total expenses of necessities")
        monthly_income_label = tkinter.Label(budget_frame, text="Enter monthly income")
        budget_duration_label = tkinter.Label(budget_frame, text="Enter duration of budget in months")
        budget_wants_label = tkinter.Label(budget_frame, text="Select what percent of monthly income to save for 'wants'")
        budget_savings_label = tkinter.Label(budget_frame, text="Select what percent of monthly income to put into savings")

        # entries
        monthly_expenses_entry = tkinter.Entry(budget_frame, textvariable=monthly_expenses)
        monthly_income_entry = tkinter.Entry(budget_frame, textvariable=monthly_income)
        budget_duration_entry = tkinter.Entry(budget_frame, textvariable=budget_duration)

        # buttons
        monthly_wants_10 = tkinter.Radiobutton(budget_frame, text="10%", variable=monthly_wants, value=0.1)
        monthly_wants_20 = tkinter.Radiobutton(budget_frame, text="20%", variable=monthly_wants, value=0.2)
        monthly_wants_30 = tkinter.Radiobutton(budget_frame, text="30%", variable=monthly_wants, value=0.3)
        monthly_savings_10 = tkinter.Radiobutton(budget_frame, text="10%", variable=monthly_savings, value=0.1)
        monthly_savings_20 = tkinter.Radiobutton(budget_frame, text="20%", variable=monthly_savings, value=0.2)
        monthly_savings_30 = tkinter.Radiobutton(budget_frame, text="30%", variable=monthly_savings, value=0.3)
        submit_button = tkinter.Button(budget_frame, text="SUBMIT", command=budget_info)

        # grid
        monthly_expenses_label.grid(row=0, column=0)
        monthly_expenses_entry.grid(row=0, column=1)
        monthly_income_label.grid(row=1, column=0)
        monthly_income_entry.grid(row=1, column=1)
        budget_duration_label.grid(row=2, column=0)
        budget_duration_entry.grid(row=2, column=1)
        budget_wants_label.grid(row=3, column=0)
        monthly_wants_10.grid(row=3, column=1)
        monthly_wants_20.grid(row=3, column=2)
        monthly_wants_30.grid(row=3, column=3)
        budget_savings_label.grid(row=4, column=0)
        monthly_savings_10.grid(row=4, column=1)
        monthly_savings_20.grid(row=4, column=2)
        monthly_savings_30.grid(row=4, column=3)
        submit_button.grid(row=5, column=1)


        def budget_info():
            info_frame = tkinter.Toplevel(main)
            info_frame.title("Budget Info")

            income = monthly_income.get()
            expenses = monthly_expenses.get()
            wants = monthly_wants.get()
            savings = monthly_savings.get()
            duration = budget_duration.get()



    def filler():
        print("You clicked me!")



    # main screen info
    username = tkinter.StringVar()
    password = tkinter.StringVar()
    
    login_button = tkinter.Button(main, text="LOGIN", command=complete_login)
    register_button = tkinter.Button(main, text="REGISTER", command=register_frame)
    continue_button = tkinter.Button(main, text="CONTINUE WITHOUT\n REGISTERING", command = budget_board) # change the command for this button
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
    db.close()