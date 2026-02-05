# 3. Persiistence CSV
# 3.1 Members — members.csv

# Fields:

#     miembro_id
#     nombre
#     documento
#     telefono
#     correo
#     plan (BÁSICO | PREMIUM | FULL)
#     fecha_inicio
#     fecha_fin_plan
#     estado (ACTIVO | INACTIVO)

import csv 

def member ():
    name = input("Enter username: ")
    document = input("Enter document: ")
    with open('miembros.csv', mode='r') as file:
        reader = csv.DictReader (file)
        for row in reader:
            if row ['name'] == name and row ['document'] == document and row ['document'] == document:
                print("Information member is: ", row ['name'], row ['document'], row ['phone'], row ['email'], row ['plan'], row ['start_date'], row ['end_date'], row ['state'])
                return True
        print("Incorrect values, please try again")
        return False
member()