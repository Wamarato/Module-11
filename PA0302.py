# 1. Get input from the user - console input
student_name = input("Enter student name: ")
subject1 = float(input("Enter mark for Programming: "))
subject2 = float(input("Enter mark for Database: "))
subject3 = float(input("Enter mark for Web Development: "))

# 2. Perform calculations
total = subject1 + subject2 + subject3
average = total / 3

# 3. Display output - console output
print("\n=== RESULTS ===")
print("Student Name:", student_name)
print("Programming:", subject1)
print("Database:", subject2)
print("Web Development:", subject3)
print("-" * 25)
print("Total Mark:", total)
print("Average Mark:", round(average, 2))

# 4. Additional output with branching
if average >= 50:
    print("Result: PASS")
else:
    print("Result: FAIL")
