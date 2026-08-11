# Student information
student_number = "ST001"
student_name = "Thabo Molefe"
age = 22
course = "Software Development"
programming_mark = 78
database_mark = 65
web_development_mark = 72

file = open("student_results.txt", "w")

file.write(f"Student Number: {student_number}")
file.write(f"Student Name: {student_name}")
file.write(f"Age: {age}")
file.write(f"Course: {course}")
file.write(f"Programming Mark: {programming_mark}")
file.write(f"Database Mark: {database_mark}")
file.write(f"Web Development Mark: {web_development_mark}")

file.close()

print("Student information saved successfully.")

file = open("student_results.txt", "r")

print("Student Information from File")
print("-----------------------------")
print(file.read())

file.close()