      # Fitness Membership Console

# 2. Login
  # When you start the apllicaiton, is asks for a username and password
   # Fields:
     # username
     # password
     # role

   #rules:
    # Validate against the csv
    # Not new user registration allowed

import csv

def login ():
    username = input("Enter username: ")
    password = input("Enter password: ")
    role = input("Enter role (admin/perssonel): ")
    with open('users.csv', mode='r') as file:
        reader = csv.DictReader (file)
        for row in reader:
            if row ['username'] == username and row ['password'] == password and row ['role'] == role: 
                print("Login successful")
                return True
        print("Incorrect values, please try again")
        return False
    
