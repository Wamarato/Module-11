
#A menu-driven student results program organized into separate functions,
#each performing one specific task. main() controls the overall flow.

from datetime import datetime

FILENAME = "student_results.txt"


def login():
    
#Asks the user for a username and password.
#Returns True if login is successful, False otherwise.
    
    print("--- LOGIN ---")
    username = input("Enter username: ")
    password = input("Enter password: ")

# Simple fixed credentials for demonstration purposes
    if username == "admin" and password == "admin123":
        print("\nLogin successful!\n")
        return True
    else:
        print("\nIncorrect username or password.\n")
        return False


def capture_student():
    
#Captures student details and subject marks from the user.
#Returns the information as a dictionary.
    
    print(" CAPTURE STUDENT ")
    student_number = input("Enter Student Number: ")
    full_name = input("Enter Full Name: ")
    course = input("Enter Course: ")

    programming = float(input("Enter Programming mark: "))
    database = float(input("Enter Database mark: "))
    web_development = float(input("Enter Web Development mark: "))

    student = {
        "student_number": student_number,
        "full_name": full_name,
        "course": course,
        "programming": programming,
        "database": database,
        "web_development": web_development,
    }

    return student


def calculate_results(student):
    
#Calculates the total, average, and final result for a student.
#Adds these values to the student dictionary and returns it.
    
    total = student["programming"] + student["database"] + student["web_development"]
    average = total / 3

    if average >= 50:
        result = "Competent"
    else:
        result = "Not Yet Competent"

    student["total"] = total
    student["average"] = average
    student["result"] = result
    student["date_saved"] = datetime.now().strftime("%d %B %Y")

    return student


def display_results(student):
    
#Displays the student's results on the console.
    
    print("\n----- STUDENT RESULTS -----")
    print(f"Student Number: {student['student_number']}")
    print(f"Student Name: {student['full_name']}")
    print(f"Course: {student['course']}")
    print(f"Programming: {student['programming']:.0f}")
    print(f"Database: {student['database']:.0f}")
    print(f"Web Development: {student['web_development']:.0f}")
    print(f"Total: {student['total']:.0f}")
    print(f"Average: {student['average']:.2f}")
    print(f"Result: {student['result']}")
    print(f"Date Saved: {student['date_saved']}")
    print("----------------------------\n")


def save_results(student):
    
#Saves the student's information to student_results.txt.
#Uses file = open(...) and file.close().
    
    file = open(FILENAME, "w")

    file.write(f"Student Number: {student['student_number']}\n")
    file.write(f"Student Name: {student['full_name']}\n")
    file.write(f"Course: {student['course']}\n")
    file.write(f"Programming: {student['programming']:.0f}\n")
    file.write(f"Database: {student['database']:.0f}\n")
    file.write(f"Web Development: {student['web_development']:.0f}\n")
    file.write(f"Total: {student['total']:.0f}\n")
    file.write(f"Average: {student['average']:.2f}\n")
    file.write(f"Result: {student['result']}\n")
    file.write(f"Date Saved: {student['date_saved']}\n")

    file.close()

    print("Results saved successfully to student_results.txt\n")


def read_results():
    
#Opens student_results.txt, reads its contents, displays it
#on the console, and closes the file correctly.
    
    try:
        file = open(FILENAME, "r")
        contents = file.read()
        file.close()

        print("\n----- FILE CONTENTS -----")
        print(contents)
        print("--------------------------\n")

    except FileNotFoundError:
        print("Error: student_results.txt not found. Please capture and save a student first.\n")


def display_menu():
    
#Displays the main menu and returns the user's choice.
    
    print("----- MAIN MENU -----")
    print("1. Capture Student and Calculate Results")
    print("2. Display Results")
    print("3. Save Results to File")
    print("4. Read Results from File")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    return choice


def main():
    
#Controls the main flow of the program.
    
    if login():
        current_student = None

        while True:
            choice = display_menu()

            if choice == "1":
                current_student = capture_student()
                current_student = calculate_results(current_student)
                print("\nStudent captured and results calculated.\n")

            elif choice == "2":
                if current_student:
                    display_results(current_student)
                else:
                    print("\nNo student captured yet. Choose option 1 first.\n")

            elif choice == "3":
                if current_student:
                    save_results(current_student)
                else:
                    print("\nNo student captured yet. Choose option 1 first.\n")

            elif choice == "4":
                read_results()

            elif choice == "5":
                print("Goodbye!")
                break

        else:
                print("\nInvalid choice. Please select 1-5.\n")
    else:
        print("Access denied. Program will now close.")


if __name__ == "__main__":
    main()