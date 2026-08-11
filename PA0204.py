# Store subjects and marks in a dictionary
subjects_marks = {
    "Programming": 78,
    "Database": 65,
    "Web Development": 72
}

# Variables to use in the loop
total_mark = 0
subject_count = 0

print("=== STUDENT MARKS ===")

# Use a for loop to display all subjects and their marks
# Also calculate total and count subjects
for subject, mark in subjects_marks.items():
    print(f"{subject}: {mark}") # Display subject and mark
    
    total_mark = total_mark + mark # 1. Calculate the total mark
    subject_count = subject_count + 1 # 2. Count the number of subjects

# 3. Display the average
average_mark = total_mark / subject_count

print("-" * 30)
print("Total Mark:", total_mark)
print("Number of Subjects:", subject_count)
print("Average Mark:", round(average_mark, 2))