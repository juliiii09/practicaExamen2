# Student Management System.

A Python application for managing student records using JSON for data persistence and CSV for data export.

## Description.

This project is a student management system that allows you to:
- Add, view, search, modify, and delete student records.
- Store data persistently in JSON format.
- Export data to CSV format.
- Validate input data (grades between 0.0-5.0, unique IDs).

## Features.

| Feature | Description |
|---------|-------------|
| **Add Student** | Register new students with ID, name, and grade |
| **List Students** | Display all students in a formatted table |
| **Search Student** | Find students by their ID |
| **Modify Student** | Update student name and/or grade |
| **Delete Student** | Remove a student with confirmation |
| **Export to CSV** | Convert JSON data to CSV format |

## Requirements.

- Python 3.6 or higher.
- No external dependencies (uses standard library only).

## Installation.

1. Navigate to the project directory:
   ```bash
   cd "PyTHON DS/Mini project json ans csv (Célula)"
   ```

2. No additional installation required - uses Python standard library.

## Usage.

Run the application:
```bash
python mini_project.py
```

## Main Menu Options.

```
========================================
           MAIN MENU
========================================
 1. Add student
 2. List students
 3. Search student by ID
 4. Modify student
 5. Delete student
 6. Export to CSV
 0. Exit
========================================
```

### Menu Options Detail.

| Option | Action |
|--------|--------|
| `1` | Add a new student (requires ID, name, grade) |
| `2` | Display all registered students |
| `3` | Search for a student by ID |
| `4` | Modify existing student data |
| `5` | Delete a student (requires confirmation) |
| `6` | Export all students to CSV file |
| `0` | Exit the application |

## Functions Reference.

### Persistence Functions.

| Function | Description |
|----------|-------------|
| `load_students()` | Loads students from `students.json` |
| `save_students(students)` | Saves student list to `students.json` |
| `export_to_csv(students)` | Exports students to `students.csv` |

### CRUD Operations.

| Function | Description |
|----------|-------------|
| `add_student(students)` | Adds a new student with validation |
| `list_students(students)` | Displays all students in tabular format |
| `search_student(students)` | Searches student by ID |
| `modify_student(students)` | Modifies existing student data |
| `delete_student(students)` | Deletes a student by ID |

### Input Validation Functions.

| Function | Description |
|----------|-------------|
| `input_id(prompt)` | Requests non-empty ID |
| `input_name(prompt)` | Requests non-empty name |
| `input_grade(prompt)` | Requests valid grade (0.0-5.0) |

## Data Validation.

- **Student ID**: Must be unique (no duplicates allowed).
- **Grade**: Must be a number between 0.0 and 5.0.
- **Name**: Cannot be empty.
- **ID**: Cannot be empty.

## Example Output.

### List Students.
```
══════════════════════════════════════════════════
ID              Nombre                              Nota
══════════════════════════════════════════════════
123456789       Juan Pérez                         4.50
987654321       María García                       3.75
══════════════════════════════════════════════════
Total: 2 students
```

### Export to CSV.
```
Successfully exported to students.csv (2 records),
```

## Notes.

- Data is automatically saved to `students.json` after each modification
- CSV export can be done manually via option 6 or automatically on exit.
- If `students.json` doesn't exist, the system starts with an empty database.
- Type hints are used throughout the code for better readability.
- All functions include error handling for robust operation.

## Error Handling.

The application handles:
- Invalid JSON format.
- File read/write errors.
- Invalid numeric input.
- Missing files (graceful degradation).

## Project Structure.

```
PyTHON DS/Mini project json ans csv (Célula)/
├── mini_project.py      # Main Python script
├── students.json        # JSON database file (auto-created)
├── students.csv         # CSV export file (auto-created)
├── diagram_of_flow.png  # Program flow diagram
└── README.md            # This file
```