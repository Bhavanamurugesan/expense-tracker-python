students = {}

def add_student():
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    marks = input("Enter marks: ")
    students[id] = {"name": name, "marks": marks}

def view_students():
    for id, info in students.items():
        print("ID:", id)
        print("Name:", info["name"])
        print("Marks:", info["marks"])
        print("------------")

def delete_student():
    id = input("Enter student ID to delete: ")
    if id in students:
        del students[id]
        print("Student deleted")
    else:
        print("Student not found")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        break