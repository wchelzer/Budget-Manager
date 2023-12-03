# Author: Wyatt Helzer
# Creation Date: 12/1/2023
# Date Last Updated: 12/1/2023
# Function: ...

#---------------------------------------------------------------------------------------------

import mysql.connector

def create_db():

    # Creates MySQL connection
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Mr_Kaboom1939"
    )

    cursor = db.cursor()

    # Creates and use
    cursor.execute("CREATE DATABASE budget_manager;")
    cursor.execute("USE budget_manager;")

    # Creates tables
    cursor.execute("""CREATE TABLE user (user_id INT NOT NULL AUTO_INCREMENT, username VARCHAR(30) NOT NULL, password VARCHAR(30) NOT NULL, monthly_income INT, 
                   expenses INT, wants FLOAT, savings FLOAT, PRIMARY KEY(user_id))""")
    # cursor.execute("""CREATE TABLE budget (budget_id INT NOT NULL AUTO_INCREMENT, user_id INT, monthly_income INT, expenses INT, wants INT, savings INT, 
    #             PRIMARY KEY (budget_id), FOREIGN KEY (user_id) REFERENCES user(user_id));""")

    db.commit()
    db.close()

if __name__ == "__main__":
    create_db()