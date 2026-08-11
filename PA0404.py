# 1. USE A LIST TO STORE STUDENT NAMES
student_name = ["Rose", "Can", "Ryn", "Amanda"]

# 2. USE A DICTIONARY TO STORE STUDENT NAME : AVERAGE MARK
student_results = {
    "Rose": 71.67,
    "Can": 85.33,
    "Ryn": 48.00,
    "Amanda": 62.50
}

def display_all_students():
    #Display all students from the LIST
    print("=== STUDENT LIST ===")
    for i, name in enumerate(student_name, 1):  # loop through list
        print(f"{i}. {name}")

def display_results():
    #Display all results from the DICTIONARY
    print("STUDENT RESULTS ")
    for name, average in student_results.items():  # loop through dictionary
        status = "Pass" if average >= 50 else "Fail"
        print(f"{name}: {average} - {status}")

def add_student():
    #Add new student to both the list and the dictionary
    name = input("Enter new student name: ")
    mark1 = float(input("Enter mark1: "))
    mark2 = float(input("Enter mark2: "))
    mark3 = float(input("Enter mark3: "))

    average = (mark1 + mark2 + mark3) / 3
    student_name.append(name)              # add to LIST
    student_results[name] = round(average, 2)  # add to DICTIONARY
    print(f"{name} added with average: {round(average, 2)}")

def search_student():
    """Search for a student in the DICTIONARY"""
    search_name = input("Enter name to search: ")
    if search_name in student_results:
        print(f"{search_name} found. Average: {student_results[search_name]}")
    else:
        print("Student not found")

# MAIN MENU
choice = 0
while choice != 5:
    print("\n=== STUDENT MANAGEMENT ===")
    print("1. Display all students - from LIST")
    print("2. Display all results - from DICTIONARY")
    print("3. Add new student")
    print("4. Search student")
    print("5. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        display_all_students()
    elif choice == 2:
        display_results()
    elif choice == 3:
        add_student()
    elif choice == 4:
        search_student()
    elif choice == 5:
        print("Exiting...")
    else:
        print("Invalid option")