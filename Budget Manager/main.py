# Author: Wyatt Helzer
# Creation Date: 12/1/2023
# Date Last Updated: 12/3/2023
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
    main.geometry("300x150")
    


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



    def register_frame():
        global register_username
        global register_password
        global register_password_verification
        
        register_screen = Toplevel(main)
        register_screen.title("Registration Page")
        register_screen.geometry("300x165")

        register_username = tkinter.StringVar()
        register_password = tkinter.StringVar()
        register_password_verification = tkinter.StringVar()

        # labels
        register_info_label = tkinter.Label(register_screen, text="Enter new login information", font=("13"))
        register_username_label = tkinter.Label(register_screen, text="Username: ", font=("13"))
        register_password_label = tkinter.Label(register_screen, text="Password: ", font=("13"))
        register_password_verification_label = tkinter.Label(register_screen, text="Confirm your password: ", font=("10"))

        # entries
        register_username_entry = tkinter.Entry(register_screen, textvariable=register_username)
        register_password_entry = tkinter.Entry(register_screen, textvariable=register_password, show="*")
        register_password_verification_entry = tkinter.Entry(register_screen, textvariable=register_password_verification, show="*")

        # button
        register_button = tkinter.Button(register_screen, text="REGISTER", command=complete_registration, width=20)

        # grid
        register_info_label.grid(row=0, column=0, columnspan=2, pady=15)
        register_username_label.grid(row=1, column=0)
        register_username_entry.grid(row=1, column=1)
        register_password_label.grid(row=2, column=0)
        register_password_entry.grid(row=2, column=1)
        register_password_verification_label.grid(row=3, column=0)
        register_password_verification_entry.grid(row=3, column=1)
        register_button.grid(row=4, column=0, columnspan=2, pady=5)




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
                    dashboard()
                    return
            else:
                print("Account doesn't exist. Please check your information or register an account")
        

    def budget_info():
            income = monthly_income.get()
            expenses = monthly_expenses.get()
            duration = budget_duration.get()
            savings_percent = monthly_savings.get()

            if(income <= 0 or expenses <= 0 or savings_percent <= 0 or duration <= 0):
                print("Please fill out all fields. Enter values greater than 0")
                return
            elif(income-expenses < 0):
                print("Your monthly income does not cover your expenses")
                return
            else:
                # calculations
                monthly_disposable = income - expenses

                new_monthly_savings = monthly_disposable * savings_percent
                total_savings = monthly_disposable * savings_percent * duration

                new_monthly_wants = monthly_disposable - new_monthly_savings
                total_wants = (monthly_disposable - new_monthly_savings) * duration

                # insert budget info into database
                cursor = db.cursor()
                query = """UPDATE user SET monthly_income=%s, monthly_expenses=%s, duration=%s, monthly_wants=%s, monthly_savings=%s, total_wants=%s, 
                        total_savings=%s WHERE username=%s AND password=%s;"""
                values = (income, expenses, duration, new_monthly_wants, new_monthly_savings, total_wants, total_savings, username.get(), password.get())
                cursor.execute(query, values)
                db.commit()
                print("Values submited!")

                info_frame = tkinter.Toplevel(main)
                info_frame.title("Budget Info")
                info_frame.geometry("250x200")
                

                # labels
                monthly_expenses_label = tkinter.Label(info_frame, text= f"Monthly expenses : ${expenses}", font=("10"))
                monthly_income_label = tkinter.Label(info_frame, text= f"Monthly income : ${income}", font=("10"))
                duration_label = tkinter.Label(info_frame, text= f"Total duration : {duration} months", font=("10"))
                monthly_wants_label = tkinter.Label(info_frame, text= f"Monthly money for 'wants' : ${new_monthly_wants}", font=("10"))
                monthly_savings_label = tkinter.Label(info_frame, text= f"Monthly savings : ${new_monthly_savings}", font=("10"))
                total_wants_label = tkinter.Label(info_frame, text= f"Total money for 'wants' : ${total_wants}", font=("10"))
                total_savings_label = tkinter.Label(info_frame, text= f"Total savings : ${total_savings}", font=("10"))

                # grid
                monthly_expenses_label.grid(row=0, column=0)
                monthly_income_label.grid(row=1, column=0)
                duration_label.grid(row=2, column=0)
                monthly_wants_label.grid(row=3, column=0)
                total_wants_label.grid(row=4, column=0)
                monthly_savings_label.grid(row=5, column=0)
                total_savings_label.grid(row=6, column=0)




    def budget_input():
        budget_frame = tkinter.Toplevel(main)
        budget_frame.title("Budget Input")

        global monthly_expenses
        global monthly_income
        global budget_duration
        global monthly_savings

        monthly_expenses = tkinter.DoubleVar()
        monthly_income = tkinter.DoubleVar()
        budget_duration = tkinter.IntVar()
        monthly_savings = tkinter.DoubleVar()

        # labels
        budget_frame_label = tkinter.Label(budget_frame, text="Enter your budget information", font=(7))
        monthly_expenses_label = tkinter.Label(budget_frame, text="Enter total expenses of necessities:")
        monthly_income_label = tkinter.Label(budget_frame, text="Enter monthly income:")
        budget_duration_label = tkinter.Label(budget_frame, text="Enter duration of budget in months:")
        budget_savings_label = tkinter.Label(budget_frame, text="Select what percent of monthly income to put into savings:")

        # entries
        monthly_expenses_entry = tkinter.Entry(budget_frame, textvariable=monthly_expenses, width=10)
        monthly_income_entry = tkinter.Entry(budget_frame, textvariable=monthly_income, width=10)
        budget_duration_entry = tkinter.Entry(budget_frame, textvariable=budget_duration, width=10)

        # buttons
        monthly_savings_10 = tkinter.Radiobutton(budget_frame, text="10%", variable=monthly_savings, value=0.1)
        monthly_savings_20 = tkinter.Radiobutton(budget_frame, text="20%", variable=monthly_savings, value=0.2)
        monthly_savings_30 = tkinter.Radiobutton(budget_frame, text="30%", variable=monthly_savings, value=0.3)
        submit_button = tkinter.Button(budget_frame, text="SUBMIT", command=budget_info, width=30)

        # grid
        budget_frame_label.grid(row=0, column=0, columnspan=3, pady=7)
        monthly_expenses_label.grid(row=1, column=0)
        monthly_expenses_entry.grid(row=1, column=1)
        monthly_income_label.grid(row=2, column=0)
        monthly_income_entry.grid(row=2, column=1)
        budget_duration_label.grid(row=3, column=0)
        budget_duration_entry.grid(row=3, column=1)
        budget_savings_label.grid(row=4, column=0)
        monthly_savings_10.grid(row=4, column=1)
        monthly_savings_20.grid(row=4, column=2)
        monthly_savings_30.grid(row=4, column=3)
        submit_button.grid(row=5, column=0, columnspan=3, pady=5)


    def info():
        print("You clicked me!")

        cursor = db.cursor()
        query = "SELECT monthly_income FROM user WHERE username=%s AND password=%s;"
        values = (username.get(), password.get())
        
        cursor.execute(query, values)
        user = cursor.fetchall()

        if(str(user[0][0]) == 'None'):
            print("No budget info")
            return
        else:
            print("Success!")

            info_frame = tkinter.Toplevel(main)
            info_frame.title("Budget Info")
            info_frame.geometry("250x200")
            
            query = """SELECT monthly_income, monthly_expenses, duration, monthly_wants, monthly_savings, total_wants, 
                    total_savings FROM user WHERE username=%s AND password=%s"""
            values = (username.get(), password.get())
            cursor.execute(query, values)
            user_info = cursor.fetchall()

            # labels
            monthly_expenses_label = tkinter.Label(info_frame, text= f"Monthly expenses: ${user_info[0][1]}", font=("10"))
            monthly_income_label = tkinter.Label(info_frame, text= f"Monthly income: ${user_info[0][0]}", font=("10"))
            duration_label = tkinter.Label(info_frame, text= f"Total duration: {user_info[0][2]} months", font=("10"))
            monthly_wants_label = tkinter.Label(info_frame, text= f"Monthly money for wants: ${user_info[0][3]}", font=("10"))
            monthly_savings_label = tkinter.Label(info_frame, text= f"Monthly savings: ${user_info[0][4]}", font=("10"))
            total_wants_label = tkinter.Label(info_frame, text= f"Total money for wants: ${user_info[0][5]}", font=("10"))
            total_savings_label = tkinter.Label(info_frame, text= f"Total savings: ${user_info[0][6]}", font=("10"))

            # grid
            monthly_expenses_label.grid(row=0, column=0)
            monthly_income_label.grid(row=1, column=0)
            duration_label.grid(row=2, column=0)
            monthly_wants_label.grid(row=3, column=0)
            monthly_savings_label.grid(row=4, column=0)
            total_wants_label.grid(row=5, column=0)
            total_savings_label.grid(row=6, column=0)
        


    def dashboard():
        dashboard_frame = tkinter.Toplevel(main)
        dashboard_frame.title("Dashboard")
        dashboard_frame.geometry("240x120")

        info_button = tkinter.Button(dashboard_frame, text="Info", command=info, width=20, height=2)
        edit_create_budget = tkinter.Button(dashboard_frame, text="Edit or Create Budget", command=budget_input, width=20, height=2)

        info_button.grid(row=0, column=0, columnspan=1, padx=43, pady=3)
        edit_create_budget.grid(row=1, column=0, columnspan=1, padx=43, pady=3)



    # main screen info
    username = tkinter.StringVar()
    password = tkinter.StringVar()
    
    login_button = tkinter.Button(main, text="LOGIN", command=complete_login, width=20) 
    register_button = tkinter.Button(main, text="REGISTER", command=register_frame, width=20)
    #continue_button = tkinter.Button(main, text="CONTINUE WITHOUT\n REGISTERING", command = budget_input) # change the command for this button
    username_label = tkinter.Label(main, text="Username: ", font=("Calibri, 13"), padx=5)
    password_label = tkinter.Label(main, text="Password: ", font=("Calibri, 13"), padx=5)
    username_entry = tkinter.Entry(main, textvariable=username)
    password_entry = tkinter.Entry(main, textvariable=password, show="*")
    
    # grid
    username_label.grid(row=0, column=0)
    username_entry.grid(row=0, column=1)
    password_label.grid(row=1, column=0)
    password_entry.grid(row=1, column=1)
    login_button.grid(row=2, column=0, columnspan=2, pady=5)
    register_button.grid(row=3, column=0, columnspan=2, pady=5)
    #continue_button.grid(row=2, column=1)
    
    
    tkinter.mainloop()
    db.close()
