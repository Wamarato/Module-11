#Use built-in modules to perform operating system, date and mathematical operations

import os
import datetime
import math


#1. Check whether student_results.txt exists.
if os.path.exists("student_results.txt"):
    print("student_results.txt exists.")
else:
    print("student_results.txt does not exist.")

#2. Display the current working directory.
print(f"Current working directory: {os.getcwd()}")

#3. Create a folder named student_records when it does not exist
if not os.path.exists("student_records"):
    os.makedirs("student_records")