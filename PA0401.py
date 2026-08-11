# 1. The purpose of the list:
# 'marks' stores the individual marks a student obtained in three subjects.
marks = [65, 72, 80]

# Variable used to accumulate the sum of all marks, starts at 0.
total = 0

# 2. The purpose of the loop:
# The for loop goes through each value in the 'marks' list, one at a time,
# so that each mark can be added to the running total.
for mark in marks:
    # 3. How the total is calculated:
    # Each mark is added to 'total' as the loop repeats.
    # After all three marks have been processed, total = 65 + 72 + 80 = 217.
    total += mark

# 4. How the average is calculated:
# The total of all marks is divided by the number of marks in the list
# (len(marks) = 3), giving average = 217 / 3 = 72.33...
average = total / len(marks)

# 5. How the final decision is made:
# An if/else statement checks whether the average is 50 or higher.
# If it is, the student has passed; otherwise, they have failed.
if average >= 50:
    print("Pass")
else:
    print("Fail")

# 6. The expected output:
# Since the average (72.33) is greater than or equal to 50,
# the condition is True, so the program prints: Pass