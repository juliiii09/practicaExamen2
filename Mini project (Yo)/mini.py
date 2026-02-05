# Student Management System.

import json # Import library for JSON handling.
import pandas as pd # Import pandas for data manipulation.
from pathlib import Path # Import Path for file path handling.

excel_file = Path("registration.xlsx")
json_file = Path("registration.json")

# Persistence functions.
def load_from_excel() -> pd.DataFrame: # Load data from Excel if it exists.
    if not excel_file.exists():
        print(f"File {excel_file} not found. Starting empty.")
        return pd.DataFrame(columns=["Cedula", "Nombre", "Nota final"])

    try:
        df = pd.read_excel(excel_file)
        # Clean: remove empty rows and duplicates.
        df = df.dropna(how="all").drop_duplicates()
        # Convert grade to float.
        df["Nota final"] = pd.to_numeric(df["Nota final"], errors="coerce")
        # Remove rows with invalid grades.
        df = df.dropna(subset=["Nota final"])
        print(f"Loaded {len(df)} students from Excel.")
        return df
    except Exception as e:
        print(f"Error loading Excel: {e}")
        return pd.DataFrame(columns=["Cedula", "Nombre", "Nota final"])

def load_from_json() -> pd.DataFrame: # Load data from JSON, fallback to Excel.
    if not json_file.exists() or json_file.stat().st_size == 0:
        print(f"File {json_file} not found or empty. Using Excel as the initial source.")
        df = load_from_excel()
        save_to_json(df)
        return df

    try:
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        df = pd.DataFrame(data)
        # Clean: remove empty rows and duplicates.
        df = df.dropna(how="all").drop_duplicates()
        # Convert grade to float.
        df["Nota final"] = pd.to_numeric(df["Nota final"], errors="coerce")
        df = df.dropna(subset=["Nota final"])
        print(f"Loaded {len(df)} students from JSON.")
        return df
    except (json.JSONDecodeError, Exception) as e:
        print(f"Error loading JSON: {e}. Falling back to Excel.")
        return load_from_excel()

def save_to_json(df: pd.DataFrame) -> None: # Save DataFrame to JSON.
    if df.empty:
        print("There is no data to save.")
        return

    try:
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(df.to_dict(orient="records"), f, ensure_ascii=False, indent=4)
        print(f"Data saved in {json_file} ({len(df)} students)")
    except Exception as e:
        print(f"Error saving JSON: {e}")

# Input validation functions.
def input_non_empty(prompt: str) -> str: # Requests a non-empty string.
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("It cannot be empty.")

def input_float(prompt: str, min_val: float = 0.0, max_val: float = 5.0) -> float: # Requests a float within a range.
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return round(value, 1)
            print(f"It must be between {min_val} and {max_val}.")
        except ValueError:
            print("Please enter a valid number.")

# CRUD operations.
def show_records(df: pd.DataFrame) -> None: # Display student records.
    if df.empty:
        print("There are no registered students.")
        return

    print("\n" + "═" * 60)
    print(f"{'Índice':<8} {'Cedula':<15} {'Nombre':<35} {'Nota final':>10}")
    print("═" * 60)

    for i, row in df.iterrows():
        print(f"{i+1:<8} {row['Cedula']:<15} {row['Nombre']:<35} {row['Nota final']:>10.1f}")
    print("═" * 60)
    print(f"Total: {len(df)} students")

def add_student(df: pd.DataFrame) -> pd.DataFrame: # Add a new student.
    print("\n Add student ")
    cedula = input_non_empty("Cedula: ")
    # Check for duplicate cedula.
    if cedula in df["Cedula"].values:
        print(f"There is already a student with an ID card {cedula}")
        return df

    nombre = input_non_empty("Nombre: ")
    nota = input_float("Nota final (0.0 - 5.0): ")

    new_row = pd.DataFrame({
        "Cedula": [cedula],
        "Nombre": [nombre],
        "Nota final": [nota]
    })
    df = pd.concat([df, new_row], ignore_index=True)
    save_to_json(df)
    print(f"Student {nombre} added (Cédula: {cedula})")
    return df

def edit_student(df: pd.DataFrame) -> pd.DataFrame: # Edit an existing student.
    if df.empty:
        print("There are no students to edit.")
        return df

    show_records(df) 

    try:
        idx = int(input("Student number to edit (1-N): ")) - 1
        if idx < 0 or idx >= len(df):
            print("Index out of range.")
            return df
    except ValueError:
        print("Invalid input.")
        return df

    print("\n Editing student:")
    print(f"Current: Cédula {df.at[idx, 'Cedula']} | Nombre: {df.at[idx, 'Nombre']} | Nota: {df.at[idx, 'Nota final']:.1f}")

    new_cedula = input(f"New ID card (Enter = keep): ").strip()
    if new_cedula:
        if new_cedula in df["Cedula"].values and new_cedula != df.at[idx, "Cedula"]:
            print("There is already a student with that ID card, not modified")
        else:
            df.at[idx, "Cedula"] = new_cedula

    new_nombre = input(f"New name (Enter = keep): ").strip()
    if new_nombre:
        df.at[idx, "Nombre"] = new_nombre

    nota_input = input(f"New note (Enter = hold): ").strip()
    if nota_input:
        try:
            new_nota = float(nota_input)
            if 0 <= new_nota <= 5:
                df.at[idx, "Nota final"] = round(new_nota, 1)
            else:
                print("Value out of range, not modified")
        except ValueError:
            print("Invalid number, not modified")

    save_to_json(df)
    print("Student updated.")
    return df

def delete_student(df: pd.DataFrame) -> pd.DataFrame: # Delete a student.
    if df.empty:
        print("There are no students to remove.")
        return df

    show_records(df)

    try:
        idx = int(input("Student number to be deleted (1-N): ")) - 1
        if idx < 0 or idx >= len(df):
            print("Index out of range.")
            return df
    except ValueError:
        print("Invalid input.")
        return df

    confirm = input(f"Delete to {df.at[idx, 'Nombre']} (Cédula {df.at[idx, 'Cedula']})? [Y/n]: ").strip().lower()
    if confirm in ("s", "si", "y", "yes"):
        df = df.drop(idx).reset_index(drop=True)
        save_to_json(df)
        print("Student deleted.")
    else:
        print("Deletion cancelled.")
    return df

# Main loop.
def main(): # Main program loop.
    df = load_from_json()

    while True:
        print("\n" + "═" * 40)
        print(" STUDENT MANAGEMENT MENU ".center(40))
        print("═" * 40)
        print(" 1. View records")
        print(" 2. Add student")
        print(" 3. Edit student")
        print(" 4. Delete student")
        print(" 0. Exit")
        print("═" * 40)

        opcion = input("Option: ").strip()

        if opcion == "1":
            show_records(df)
        elif opcion == "2":
            df = add_student(df)
        elif opcion == "3":
            df = edit_student(df)
        elif opcion == "4":
            df = delete_student(df)
        elif opcion == "0":
            print("\nSaving final changes...")
            save_to_json(df)
            print("See you later!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__": 
    main()  # Call to main function to start the program.