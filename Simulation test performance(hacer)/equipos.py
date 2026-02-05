# Control de inventario de equipos
import csv # Importar libreria CSV para manejar archivos
import os # Importar libreria OS para manejo de archivos y rutas

def inicializar_csv_equipos(): # Crear archivo CSV si no existe
    if not os.path.exists("equipos.csv"):
        with open("equipos.csv", "w", newline='', encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["id", "nombre", "estado"]) # estado: disponible / prestado / dañado / mantenimiento

def cargar_equipos(): # Cargar lista de equipos desde CSV
    equipos = []
    try:
        with open("equipos.csv", mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                equipos.append(fila)
    except FileNotFoundError:
        print("Error: No se encontró equipos.csv")
    return equipos

def guardar_todos_equipos(equipos): # Guardar lista completa de equipos en CSV
    with open("equipos.csv", mode="w", newline='', encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["id", "nombre", "estado"])
        for eq in equipos:
            escritor.writerow([eq["id"], eq["nombre"], eq["estado"]])

def ver_equipos(): # Ver todos los equipos
    equipos = cargar_equipos()

    if not equipos:
        print("\nNo hay equipos registrados.\n")
        return

    print("\n LISTADO DE EQUIPOS ")
    print("-" * 40)
    for eq in equipos:
        print(f"ID: {eq['id']} | Nombre: {eq['nombre']} | Estado: {eq['estado']}")
    print("-" * 40)

def agregar_equipo(): # Agregar nuevo equipo
    print("\n AGREGAR NUEVO EQUIPO ")

    id_equipo = input("Ingrese un ID único para el equipo: ").strip()
    nombre = input("Ingrese nombre del equipo: ").strip()
    
    estado = "disponible"  # Por defecto

    with open("equipos.csv", mode="a", newline='', encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([id_equipo, nombre, estado])

    print(f"\nEquipo '{nombre}' agregado exitosamente.\n")

def eliminar_equipo(): # Eliminar equipo por ID
    print("\n ELIMINAR EQUIPO ")
    equipos = cargar_equipos()
    if not equipos:
        print("\nNo hay equipos para eliminar.\n")
        return
    
    id_borrar = input("\nIngrese el ID del equipo a eliminar: ").strip()

    equipos_actualizados = [eq for eq in equipos if eq["id"] != id_borrar]

    if len(equipos_actualizados) == len(equipos):
        print("No existe un equipo con ese ID.\n")
        return

    guardar_todos_equipos(equipos_actualizados)

    print(f"Equipo con ID '{id_borrar}' eliminado correctamente.\n")

def cambiar_estado_equipo(): # Cambiar estado de un equipo
    print("\n CAMBIAR ESTADO DEL EQUIPO ")
    equipos = cargar_equipos()

    if not equipos:
        print("\nNo hay equipos registrados.\n")
        return

    id_equipo = input("\nIngrese el ID del equipo para cambiar su estado: ").strip()

    estados_validos = ["disponible", "prestado", "dañado", "mantenimiento"]

    for eq in equipos:
        if eq["id"] == id_equipo:

            print(f"\nEstado actual: {eq['estado']}")
            print("Estados válidos:", estados_validos)

            nuevo_estado = input("Ingrese nuevo estado: ").strip().lower()

            if nuevo_estado not in estados_validos:
                print("Estado inválido.\n")
                return

            eq["estado"] = nuevo_estado
            guardar_todos_equipos(equipos)
            print("\nEstado actualizado correctamente.\n")
            return

    print("No existe un equipo con ese ID.\n")