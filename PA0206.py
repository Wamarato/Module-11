# Use a while loop to display menu repeatedly
choice = 0 # Initialize choice to enter loop

while choice != 5: # Loop continues until user selects 5
    print("\nSTUDENT RESULTS MANAGEMENT SYSTEM")
    print("1. Capture student information")
    print("2. Display student results")
    print("3. Save results to file")
    print("4. Read results from file")
    print("5. Exit")
    print("-" * 40)
    
    # Get user input
    choice = int(input("Enter your choice (1-5): "))
    
    # Use branching statements to process menu selection
    if choice == 1:
        print("Option 1 selected: Capture student information")
    elif choice == 2:
        print("Option 2 selected: Display student results")
    elif choice == 3:
        print("Option 3 selected: Save results to file")
    elif choice == 4:
        print("Option 4 selected: Read results from file")
    elif choice == 5:
        print("Exiting program... Goodbye!")
    else:
        # 3. Display error message for invalid option
        print("Error: Invalid option. Please enter a number between 1 and 5.")
