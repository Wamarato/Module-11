def login():

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == "admin" and password == "Python123":
        print("Login successful.")
        return True
    else:
        print("Login failed.")
        return False


def capture_student():

    student = {}

    # Capture student information
    student["number"] = input("Enter Student Number: ")
    student["name"] = input("Enter Student Name: ")
    student["surname"] = input("Enter Student Surname: ")
    student["age"] = int(input("Enter Student Age: "))
    student["course"] = input("Enter Course Name: ")

    # Capture subject marks
    student["programming"] = float(input("Enter Programming Mark: "))
    student["database"] = float(input("Enter Database Mark: "))
    student["web"] = float(input("Enter Web Development Mark: "))

    return student


def calculate_results(student):
    """
    Calculates the student's total, average,
    and determines whether the student is competent.
    """

    # Calculate the total mark
    total = student["programming"] + student["database"] + student["web"]

    # Calculate the average mark
    average = total / 3

    # Determine the final result
    if average >= 50:
        result = "Competent"
    else:
        result = "Not Yet Competent"

    student["total"] = totalD
    student["average"] = average
    student["result"] = result

    return student


def display_results(student):

    # Display student details
    print("STUDENT RESULTS")
    print("-------------------------")
    print(f"Student Number: {student['number']}")
    print(f"Student Name: {student['name']} {student['surname']}")
    print(f"Course: {student['course']}")
    print(f"Programming: {student['programming']}")
    print(f"Database: {student['database']}")
    print(f"Web Development: {student['web']}")
    print(f"Total: {student['total']}")
    print(f"Average: {student['average']:.2f}")
    print(f"Result: {student['result']}")


def main():
    # Login before accessing the system
    if login():

        # Capture student details
        student = capture_student()

        # Calculate student results
        student = calculate_results(student)

        # Display the results
        display_results(student)


# Start the program
main()
