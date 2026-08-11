def string_demo():
    #Demonstrate different string functions
    
    # 1. GET INPUT - console input
    full_name = input("Enter student full name: ") # e.g. " Rose Williams "
    student_id = input("Enter student ID: ") # e.g. "STU-2026-001"
    feedback = input("Enter feedback comment: ") # e.g. "good work in programming"
    
    print(" ORIGINAL DATA ")
    print("Name:", full_name)
    print("ID:", student_id)
    print("Feedback:", feedback)
    
    print("STRING FUNCTIONS APPLIED ===")
    
    # 2. strip() - Remove spaces from start and end
    clean_name = full_name.strip()
    print("1. strip():", clean_name)
    
    # 3. title() - First letter of each word capital
    title_name = clean_name.title()
    print("2. title():", title_name)
    
    # 4. upper() - Convert to uppercase
    upper_id = student_id.upper()
    print("3. upper():", upper_id)
    
    # 5. lower() - Convert to lowercase
    lower_feedback = feedback.lower()
    print("4. lower():", lower_feedback)
    
    # 6. len() - Get length of string
    name_length = len(clean_name)
    print("5. len(): Name has", name_length, "characters")
    
    # 7. replace() - Replace text
    new_feedback = feedback.replace("good", "excellent")
    print("6. replace():", new_feedback)
    
    # 8. split() - Split string into list
    name_parts = clean_name.split(" ") # split by space
    print("7. split():", name_parts)
    
    # 9. find() - Find position of text
    position = student_id.find("2026")
    print("8. find(): '2026' found at position", position)
    
    # 10. startswith() and endswith()
    if student_id.startswith("STU"):
        print("9. startswith(): Valid student ID format")
    
    if student_id.endswith("001"):
        print("10. endswith(): ID ends with 001")

# Run the program
string_demo()
