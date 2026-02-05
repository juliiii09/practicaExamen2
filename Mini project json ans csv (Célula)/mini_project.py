# Student Management System.

import json # Import library for JSON handling.
import os # Import library for operating system interactions.
import csv # Import library for CSV handling.
from typing import List, Dict # Import types for type hinting.

json_file = "students.json"
csv_file = "students.csv"

# Persistence functions.
def load_students() -> List[Dict]: # Load students from a JSON file.
    if not os.path.exists(json_file):
        return []
    try:
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Basic structure validation.
            if not isinstance(data, list):
                print("Invalid JSON format. Starting empty.")
                return []
            return data
    except (json.JSONDecodeError, Exception) as e:
        print(f"Error loading {json_file}: {e}")
        return []

def save_students(students: List[Dict]) -> None: # Save students to a JSON file.
    try:
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(students, f, indent=4, ensure_ascii=False)
        print(f"Saved data ({len(students)} students)")
    except Exception as e:
        print(f"Error saving {json_file}: {e}")

def export_to_csv(students: List[Dict]) -> None: # Export students to a CSV file.
    if not students:
        print("There are no students to export..")
        return

    fieldnames = ["id", "name", "grade"]

    try:
        with open(csv_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)
        print(f"Successfully exported to {csv_file} ({len(students)} records)")
    except Exception as e:
        print(f"Error exporting to CSV: {e}")

# Auxiliary functions with validated input.
def input_id(prompt: str = "ID: ") -> str: # Requests a non-empty ID.
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("The ID cannot be empty.")

def input_name(prompt: str = "Nombre: ") -> str: # Requests a non-empty name.
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("The name cannot be empty.")

def input_grade(prompt: str = "Nota (0.0 - 5.0): ") -> float: # Requests a valid grade between 0.0 and 5.0.
    while True:
        try:
            value = float(input(prompt))
            if 0 <= value <= 5:
                return round(value, 2)  # we round to 2 decimal places.
            print("The score must be between 0.0 and 5.0.")
        except ValueError:
            print("Please enter a valid number.")

# CRUD operations.
def add_student(students: List[Dict]) -> None: # Adds a new student.
    print("\n Add student")
    student_id = input_id()

    # Check for duplicates.
    if any(s["id"] == student_id for s in students):
        print(f"There is already a student with ID {student_id}")
        return

    name = input_name()
    grade = input_grade()

    students.append({"id": student_id, "name": name, "grade": grade})
    save_students(students)
    print(f"Student {name} successfully added (ID: {student_id})")

def list_students(students: List[Dict]) -> None: # Lists all students.
    if not students:
        print("There are no registered students.")
        return

    print("\n" + "═" * 50)
    print(f"{'ID':<15} {'Nombre':<35} {'Nota':>6}")
    print("═" * 50)

    for s in students:
        print(f"{s['id']:<15} {s['name']:<35} {s['grade']:>6.2f}")
    print("═" * 50)
    print(f"Total: {len(students)} students")

def search_student(students: List[Dict]) -> None: # Searches for a student by ID.
    student_id = input_id("ID to search: ")
    for s in students:
        if s["id"] == student_id:
            print(f"\n {s['name']}  |  Nota: {s['grade']:.2f}")
            return
    print(f"No student with ID found {student_id}")

def modify_student(students: List[Dict]) -> None: # Modifies a student's name and/or grade.
    student_id = input_id("ID to be modified: ")

    for s in students:
        if s["id"] == student_id:
            print(f"\n Current: {s['name']}  |  Nota: {s['grade']:.2f}")

            new_name = input(f"New name (Enter = keep): ").strip()
            if new_name:
                s["name"] = new_name

            grade_input = input(f"New note (Enter = hold): ").strip()
            if grade_input:
                try:
                    new_grade = float(grade_input)
                    if 0 <= new_grade <= 5:
                        s["grade"] = round(new_grade, 2)
                    else:
                        print("Note out of range, unmodified")
                except ValueError:
                    print("Invalid value, not modified")

            save_students(students)
            print("Current student.")
            return

    print(f"No student with ID found {student_id}")

def delete_student(students: List[Dict]) -> None: # Deletes a student by ID.
    student_id = input_id("ID to be deleted: ")

    for i, s in enumerate(students):
        if s["id"] == student_id:
            confirm = input(f"Deleted to {s['name']} (ID {student_id})? [y/n]: ").strip().lower()
            if confirm in ("s", "si", "y", "yes"):
                students.pop(i)
                save_students(students)
                print("Student removed.")
            else:
                print("Operation canceled.")
            return

    print(f"No student with ID found {student_id}")

# Main menu.
def main(): # Main function to run the student management system.
    students = load_students()
    print("Student Management System".center(50, "═"))

    while True:
        print("\n" + "═" * 40)
        print(" Main Menu ".center(40))
        print("═" * 40)
        print(" 1. Add student")
        print(" 2. List students")
        print(" 3. Search student by ID")
        print(" 4. Modify student")
        print(" 5. Delete student")
        print(" 6. Export to CSV")
        print(" 0. Exit")
        print("═" * 40)

        opcion = input("Opción: ").strip()

        if opcion == "1":
            add_student(students)
        elif opcion == "2":
            list_students(students)
        elif opcion == "3":
            search_student(students)
        elif opcion == "4":
            modify_student(students)
        elif opcion == "5":
            delete_student(students)
        elif opcion == "6":
            export_to_csv(students)
        elif opcion == "0":
            print("\nSaving changes...")
            save_students(students)
            print("See you later!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__": 
    main()  # Call to main function to start the program.