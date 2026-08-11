try:
    student_name = input("Enter Student Name: ")
    mark = float(input("Enter Student Mark: "))

    if mark >= 50:
        print(f"{student_name} has passed.")
    else:
        print(f"{student_name} has failed.")

except ValueError:
    print("Error: Please enter a valid numeric mark.")