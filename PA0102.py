#Sample data these can be changed 

student_name ="Rose"
student_surname ="Abraham"
course_name ="Diploma in information technology"
registration_fee =2500.5678
prog_mark_str ="85.3"
db_mark_str ="67.9"
web_mark_str ="92.5"

# 1.join first name to surname 
full_name =student_name + " + student_surname"
print("1. full name: ", full_name)

# 2. convert course name to uppercase 
course_upper = course_name .upper()
print("2. course name uppercase:", course_upper)

#3. display number of characters in full name 
char_count = len(full_name)
print("3. number of Characters in full name:", char_count)

#4. Round registration fee to 2 decimal places 
fee_rounded = round(registration_fee, 2)
print ("4. Registration Fee Rounded :", fee_rounded)

#5. convert marks entered as string to floating-point numbers
prog_mark = float(prog_mark_str)
db_mark =float(db_mark_str)
web_mark =float(web_mark_str)
print("5. Marks converted to float:", prog_mark, db_mark, web_mark)

#6. Display full information using a f-string
print("6.  Student Info:", f"Name: {full_name}, Course: {course_upper}, Fee: R{fee_rounded}")

