# Student information 

#1. Assign a value to each variable with suitable data types 
student_number = 1111                #int
student_name = "Rose"                #str
student_surname = "Abraham"          #str
student_age = 21                     #int
Course_name ="Diploma in IT"         #str
full_time_status =True               #bool
programming_mark= 85.5               #float
Database_mark = 78.0                 #float 
web_development_mark =92.5           #float
Registration_fee =2500               #float 

print(" student information ")

#2. Display the value of each variable 
print("Student Number:", student_number)
print("Student Name:", student_name)
print("Student Surname:",  student_name)
print("Student Age:", student_age)
print("Course Name:", Course_name)
print("Full Time Status:", full_time_status)
print("Programming Mark:L", programming_mark)
print("Database Mark:", Database_mark)
print("Web Development Mark:", web_development_mark)
print("Registration Fee:", Registration_fee)

print("\n Data type of each variable ")
#3. Display the data type of each variable using type()

print("student_number:", type(student_number))
print( "student_name:", type( student_name))
print(" student_name:",type( student_name))
print(" student_age:", type( student_age))
print("Course_name:",type(Course_name))
print("full_time_status:",type(full_time_status))
print("programming_mark:",type(programming_mark))
print("Database_mark:",type(Database_mark))
print("web_development_mark:",type(web_development_mark))
print("Registration_fee:", type(Registration_fee))

print("\n type conversion")
#4. Convert at least one variable to another type 
#convert int to str
age_as_string =str (student_age)
print("Student age converted to string:", age_as_string, "type:", type(age_as_string))

#convert float to int 
program_mark_as_int =int (programming_mark)
print ("Programming mark converted into int:", program_mark_as_int, "type:", type(program_mark_as_int))

#convert bool into int 
status_as_int =int(full_time_status)
print("Full-Time status converted to int:", status_as_int, "type:", type(status_as_int))