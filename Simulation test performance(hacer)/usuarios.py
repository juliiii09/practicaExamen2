# Control de usuarios que ingresan al programa
import csv # Importar libreria CSV para manejar archivos
import os # Importar libreria OS para manejo de archivos y rutas

def inicializar_csv(): # Crear archivo CSV si no existe
    if not os.path.exists("usuarios.csv") or os.path.getsize("usuarios.csv") == 0:
        with open("usuarios.csv", "w", newline='', encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["name", "password", "role"])

def login(): # Función de inicio de sesión
    usuarios = {} # Diccionario para almacenar usuarios
    try:
        with open("usuarios.csv", mode="r", encoding="utf-8") as archivo: # Abrir archivo CSV
            lector = csv.DictReader(archivo)
            for fila in lector:
                usuarios[fila["name"].strip().lower()] = {
                    "password": fila["password"].strip(),
                    "role": fila["role"].strip().lower(),
                }
    except FileNotFoundError:
        print("Error: usuarios.csv no encontrado.")
        return None

    print("\n INICIO DE SESIÓN ")
    nombre_usuario = input("Ingrese su nombre de usuario: ").strip().lower()
    contrasena = input("Ingrese su contraseña: ").strip()

    if nombre_usuario in usuarios and usuarios[nombre_usuario]["password"] == contrasena:
        rol = usuarios[nombre_usuario]["role"]
        print(f"\nBienvenido {nombre_usuario}. Rol detectado: {rol}\n")
        return rol
    else:
        print(" Usuario o contraseña incorrectos.\n")
        return None
    
def crear_usuario(): # Función para crear un nuevo usuario
    print("\n CREAR NUEVO USUARIO ")

    while True: # Bucle para validar nombre de usuario
        nombre_usuario = input("Ingrese el nuevo nombre de usuario: ").strip().lower()
        if nombre_usuario == "":
            print("El nombre no puede estar vacío.")
            continue
        break
    contrasena = input("Ingrese la contraseña para el nuevo usuario: ").strip()
    roles_validos = ["admin", "instructor", "student", "personnel"]

    while True: # Bucle para validar rol
        rol = input("Ingrese el rol (admin / instructor / student / personnel): ").strip().lower()
        if rol not in roles_validos:
            print("Rol inválido. Intente de nuevo.")
            continue
        break

    with open("usuarios.csv", mode="a", newline='', encoding="utf-8") as archivo: # Agregar nuevo usuario al CSV
        escritor = csv.writer(archivo)
        escritor.writerow([nombre_usuario, contrasena, rol])

    print(f" Usuario '{nombre_usuario}' creado exitosamente.\n")

def borrar_usuario(nombre_usuario): # Función para borrar un usuario existente
    usuarios = []
    encontrado = False
    try:
        with open("usuarios.csv", mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                if fila["name"].strip().lower() != nombre_usuario.strip().lower():
                    usuarios.append(fila)
                else:
                    encontrado = True
    except FileNotFoundError:
        print("Error: usuarios.csv no encontrado.")
        return

    if not encontrado:
        print(f" Usuario '{nombre_usuario}' no encontrado.\n")
        return

    with open("usuarios.csv", mode="w", newline='', encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["name", "password", "role"])
        escritor.writeheader()
        for usuario in usuarios:
            escritor.writerow(usuario)

    print(f" Usuario '{nombre_usuario}' borrado exitosamente.\n")

def listar_usuarios(): # Función para listar todos los usuarios
    try:
        with open("usuarios.csv", mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            print("\n LISTA DE USUARIOS ")
            for fila in lector:
                print(f"Nombre: {fila['name']}, Rol: {fila['role']}")
            print()
    except FileNotFoundError:
        print("Error: usuarios.csv no encontrado.\n")