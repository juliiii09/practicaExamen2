# User control in the application

import csv # Imoport library csv for management
import sys 

file = "users.csv" # Variable for file csv

def load(): # Function for load file csv
    try:
        with open(file, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                return row ["user"], row["password"], row["role"]
    except FileNotFoundError:
        print("File not found")

def login(): # Function for login as admin
    user = input("Enter user: ")
    password = input("Enter password: ")
    role = input("Enter role: ")

    if user == user and password == password and role == role:
        print("Login successfully")
        return True
    else:
        print("User or password incorrect")
        return False