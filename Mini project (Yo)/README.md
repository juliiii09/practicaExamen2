# Student Management System.

A simple command-line Python application for managing student records with CRUD (Create, Read, Update, Delete) operations and data persistence.

## Description.

This project is a **Mini Project** developed in Python that allows educational institutions or teachers to manage student information. The system stores student records including:
- **Cédula** (Identification Number).
- **Nombre** (Student Name).
- **Nota Final** (Final Grade: 0.0 - 5.0).

## Features.

- **View Records**: Display all registered students in a formatted table.
- **Add Student**: Register new students with validation.
- **Edit Student**: Modify existing student information.
- **Delete Student**: Remove students from the system.
- **Data Persistence**: Automatic saving to JSON with Excel backup.
- **Input Validation**: Ensures data integrity (no empty fields, valid grades).

## Technologies Used.

- **Python 3.x**
- **pandas**: Data manipulation and Excel file handling.
- **JSON**: Data storage format.
- **pathlib**: File path handling.

## How to Run.

1. Make sure you have Python installed (version 3.6 or higher).
2. Install the required dependency:
   ```bash
   pip install pandas openpyxl
   ```
3. Run the application:
   ```bash
   python mini.py
   ```

## User Guide.

When you run the application, you'll see a menu with the following options:

| Option | Description |
|--------|-------------|
| `1` | View all student records |
| `2` | Add a new student |
| `3` | Edit an existing student |
| `4` | Delete a student |
| `0` | Exit the application |

### Adding a Student.
1. Select option `2` from the menu.
2. Enter the student's Cédula (ID number).
3. Enter the student's name.
4. Enter the final grade (0.0 - 5.0).

### Editing a Student.
1. Select option `3` from the menu.
2. View the list of students with their indices.
3. Enter the number of the student to edit.
4. Press Enter to keep current values or enter new ones.

### Deleting a Student.
1. Select option `4` from the menu.
2. View the list of students.
3. Enter the number of the student to delete.
4. Confirm deletion by typing `Y` or `yes`.

## Data Format.

### JSON Structure.
```json
[
  {
    "Cedula": 20123456,
    "Nombre": "Maria Jose Gonzalez Perez",
    "Nota final": 2.8
  }
]
```

### Column Description.
| Column | Type | Description |
|--------|------|-------------|
| Cédula | Integer/String | Unique student identification number |
| Nombre | String | Student's full name |
| Nota final | Float | Final grade (0.0 to 5.0) |

## Functions Overview.

### Persistence Functions.
- `load_from_excel()`: Loads data from Excel file.
- `load_from_json()`: Loads data from JSON file (primary).
- `save_to_json()`: Saves DataFrame to JSON file.

### Validation Functions.
- `input_non_empty()`: Ensures non-empty user input.
- `input_float()`: Validates float input within grade range.

### CRUD Functions.
- `show_records()`: Displays all students in a formatted table.
- `add_student()`: Adds a new student to the system.
- `edit_student()`: Modifies existing student data.
- `delete_student()`: Removes a student from the system.

## Technical Details.

- **Data Cleaning**: Automatically removes empty rows and duplicates.
- **Automatic Backup**: Falls back to Excel if JSON is corrupted or missing.
- **Grade Rounding**: Grades are rounded to 1 decimal place.
- **Duplicate Prevention**: Prevents duplicate Cédula entries.

## Notes.

- The system automatically creates `registration.json` if it doesn't exist.
- Excel files (`.xlsx`) require `openpyxl` library to be installed.
- All changes are automatically saved after modification operations.
- Invalid grades are automatically filtered out.

## Project Structure.

```
PyTHON DS/Mini project (Yo)/
├── mini.py              # Main application file
├── README.md            # This file
├── registration.json    # Data storage file (auto-generated)
└── registration.xlsx    # Excel backup file (optional)
```