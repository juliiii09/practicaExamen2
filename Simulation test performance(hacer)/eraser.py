# User control in the application

import csv
import sys  # Necesario para salir del programa

file = "users.csv"  # Archivo con los usuarios

def load_users():
    """Carga todos los usuarios del archivo CSV y los devuelve como diccionario"""
    users = {}
    try:
        with open(file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Suponiendo que el CSV tiene las columnas: user,password,role
                users[row["user"]] = {
                    "password": row["password"],
                    "role": row["role"]
                }
        return users
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{file}'")
        return {}
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return {}

def login():
    """Función de inicio de sesión con máximo 3 intentos"""
    users = load_users()
    
    if not users:
        print("No hay usuarios registrados o hubo un error al cargar el archivo.")
        sys.exit(1)  # Sale del programa con código de error

    max_intentos = 3
    intentos = 0

    print("=== INICIO DE SESIÓN ===")
    
    while intentos < max_intentos:
        print(f"\nIntento {intentos + 1} de {max_intentos}")
        username = input("Usuario: ").strip()
        password = input("Contraseña: ").strip()

        if username in users:
            if users[username]["password"] == password:
                print(f"\n¡Bienvenido, {username}! ({users[username]['role']})")
                return True, username, users[username]["role"]
            else:
                print("Contraseña incorrecta.")
        else:
            print("Usuario no encontrado.")

        intentos += 1
        restantes = max_intentos - intentos
        if restantes > 0:
            print(f"Te quedan {restantes} intento(s).")
        else:
        print("\n¡Has agotado los 3 intentos!")
        print("Acceso denegado. El programa se cerrará.")
        sys.exit(1)  # Termina la aplicación

# Ejemplo de uso
if __name__ == "__main__":
    exito, usuario, rol = login()
    if exito:
        print("Sesión iniciada correctamente.")
        # Aquí puedes continuar con el resto de tu aplicación