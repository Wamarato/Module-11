# Arithmetic, comparison and logical operations

#Define the three subject marks
programming_mark = 85.5
database_mark =78.0
web_development_mark = 92.5

print("student marks")
print("Programming Mark:", programming_mark)
print("Database Mark:", database_mark)
print("Web Development Mark:", web_development_mark)
print("-" * 40)

#1. Calculating the total mark - addition operator +
total_mark = programming_mark + database_mark + web_development_mark
print("1. Total mark:", total_mark)

#2. Calculate average mark- Division operator
average_mark = total_mark /3
print("2. average mark:", round(average_mark, 2))

#3. Determine the highest mark 
highest_mark = max(programming_mark, database_mark, web_development_mark)
print("3.Highest Mark:", highest_mark)

#4. Determine the lowest mark 
lowest_mark =min(programming_mark, database_mark, web_development_mark)
print("4. Lowest Mark:", lowest_mark)

#5. check weather average >= 50 - Greater than or equal to >=
passed_average = average_mark >= 50
print ("5. is average>=50?", passed_average)

#6. Check weather all 3 marks >= 40 - and  operator
all_pass =(programming_mark >= 40) and (database_mark >= 40) and (web_development_mark >= 40)
print("6. Are All marks >=40?", all_pass)

#7. Check weather at least one mark >= 75 - or operator 
has_distinction = (programming_mark >= 75) or (database_mark >=75) or (web_development_mark >=75)
print("7.Is at least one mark >=75?", has_distinction)

#8. Using all required operators 
print("\n=== all required operators demonstrated ===")
print("Addition + :, total-mark + database_mark")
print("Division / :", total_mark/3)
print("Greater than or equal to >=:", average_mark >= 50)
print("Less than <:", lowest_mark <80)
print("Equal to == :", highest_mark == web_development_mark)
print("and :", all_pass)
print("or :", has_distinction)
print("not:", not average_mark)