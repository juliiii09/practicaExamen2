# Herramienta de consola para gestionar el inventario de equipos
from usuarios import (inicializar_csv, login, crear_usuario, borrar_usuario, listar_usuarios) # Importar funciones de usuarios.py
from equipos import ( inicializar_csv_equipos, ver_equipos, agregar_equipo, eliminar_equipo, cambiar_estado_equipo) # Importar funciones de equipos.py

def menu_prestamos():
    print("\n*** Menú de préstamos (pendiente por implementar) ***\n")

def menu_devoluciones():
    print("\n*** Menú de devoluciones (pendiente por implementar) ***\n")

def menu_reportes():
    print("\n*** Menú de reportes (pendiente por implementar) ***\n")

def solicitar_prestamo():
    print("\n*** Solicitar préstamo (pendiente por implementar) ***\n")

def main(): # Función para menu inicial
    inicializar_csv()

    while True: # Bucle del menú inicial
        print("\n MENÚ INICIAL ")
        print("1. Iniciar sesión")
        print("2. Crear nuevo usuario")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            rol = login()
            if rol:
                menu_principal(rol)
        elif opcion == "2":
            crear_usuario()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.\n")

def menu_principal(rol_usuario): # Menú principal según rol
    while True: # Bucle del menú principal
        print("\n MENÚ PRINCIPAL ")
        print(f"Rol actual: {rol_usuario}\n")
        if rol_usuario == "admin": # Menú para admin
            print("1. Gestión de usuarios")
            print("2. Gestión de equipos")
            print("3. Gestión de préstamos")
            print("4. Gestión de devoluciones")
            print("5. Gestión de reportes")
            print("0. Salir")
        elif rol_usuario == "instructor": # Menú para instructor
            print("1. Ver equipos asignados")
            print("2. Solicitar equipo adicional")
            print("0. Salir")
        elif rol_usuario == "student": # Menú para student
            print("1. Ver equipos disponibles")
            print("2. Solicitar equipo")
            print("0. Salir")
        elif rol_usuario == "personnel": # Menú para personnel
            print("1. Registrar préstamos")
            print("2. Registrar devoluciones")
            print("3. Registrar reportes")
            print("0. Salir")
        opcion = input("\nSeleccione una opción: ").strip()

        if rol_usuario == "admin":
            if opcion == "1":
                menu_usuarios()
            elif opcion == "2":
                menu_equipos()
            elif opcion == "3":
                menu_prestamos()
            elif opcion == "4":
                menu_devoluciones()
            elif opcion == "5":
                menu_reportes()
            elif opcion == "0":
                print("Cerrando sesión...")
                break
            else:
                print("Opción inválida.\n")

        elif rol_usuario == "instructor":
            if opcion == "1":
                ver_equipos()
            elif opcion == "2":
                solicitar_prestamo()
            elif opcion == "0":
                print("Cerrando sesión...")
                break
            else:
                print("Opción inválida.\n")

        elif rol_usuario == "student":
            if opcion == "1":
                ver_equipos()
            elif opcion == "2":
                solicitar_prestamo()
            elif opcion == "0":
                print("Cerrando sesión...")
                break
            else:
                print("Opción inválida.\n")

        elif rol_usuario == "personnel":
            if opcion == "1":
                menu_prestamos()
            elif opcion == "2":
                menu_devoluciones()
            elif opcion == "3":
                menu_reportes()
            elif opcion == "0":
                print("Cerrando sesión...")
                break
            else:
                print("Opción inválida.\n")


def menu_usuarios(): # Menú de gestión de usuarios
    inicializar_csv() # 
    while True: # Bucle del menú de usuarios
        print("\n MENÚ DE USUARIOS ")
        print("1. Ver usuarios")
        print("2. Crear usuario")
        print("3. Eliminar usuario")
        print("0. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_usuarios()
        elif opcion == "2":
            crear_usuario()
        elif opcion == "3":
            borrar_usuario()
        elif opcion == "0":
            print("Volviendo...\n")
            break
        else:
            print("Opción inválida.\n")

def menu_equipos(): # Menú de gestión de equipos

    while True: # Bucle 
        print("\n MENÚ DE EQUIPOS ")
        print("1. Ver equipos")
        print("2. Agregar equipo")
        print("3. Eliminar equipo")
        print("4. Cambiar estado del equipo")
        print("0. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ver_equipos()
        elif opcion == "2":
            agregar_equipo()
        elif opcion == "3":
            eliminar_equipo()
        elif opcion == "4":
            cambiar_estado_equipo()
        elif opcion == "0":
            print("Volviendo...\n")
            break
        else:
            print("Opción inválida.\n")

main() # Iniciar programa