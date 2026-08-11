def capture_student():
    #Capture student details from the console and display them
    
    print("=== ENTER STUDENT DETAILS ===")
    student_number = input("Enter student number: ")
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    age = input("Enter age: ")
    course_name = input("Enter course name: ")
    programming_mark = input("Enter programming mark: ")
    database_mark = input("Enter database mark: ")
    web_dev_mark = input("Enter web development mark: ")

    print("\n=== STUDENT INFORMATION CAPTURED ===")
    print(f"Student Number   : {student_number}")
    print(f"Name             : {name}")
    print(f"Surname          : {surname}")
    print(f"Age              : {age}")
    print(f"Course           : {course_name}")
    print(f"Programming Mark : {programming_mark}")
    print(f"Database Mark    : {database_mark}")
    print(f"Web Dev Mark     : {web_dev_mark}")


# Run it
capture_student()