students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    if not name or not roll:
        print("Error: Name and roll number cannot be empty!")
        return
    students.append({"roll": roll, "name": name})
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found!")
    else:
        print("\n--- Student List ---")
        for s in students:
            print(f"Roll: {s['roll']} | Name: {s['name']}")

def update_student():
    roll = input("Enter roll number to update: ")
    for s in students:
        if s["roll"] == roll:
            s["name"] = input("Enter new name: ")
            print("Student updated successfully!")
            return
    print("Error: Student not found!")

def delete_student():
    roll = input("Enter roll number to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted successfully!")
            return
    print("Error: Student not found!")

def student_menu():
    while True:
        print("\n--- Student Module ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Back to Main Menu")
        choice = input("Enter choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")
