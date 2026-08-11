from datetime import datetime


def save_results():
    """
    Collects student result information and saves it to
    student_results.txt using file = open(...) and file.close()
    """

    # ----- Get student details -----
    student_number = input("Enter Student Number: ")
    full_name = input("Enter Full Name: ")
    course = input("Enter Course: ")

    # ----- Get subject marks -----
    programming = float(input("Enter Programming mark: "))
    database = float(input("Enter Database mark: "))
    web_development = float(input("Enter Web Development mark: "))

    # Calculations 
    total = programming + database + web_development
    average = total / 3

    if average >= 50:
        result = "Competent"
    else:
        result = "Not Yet Competent"

    #  Get current date
    date_saved = datetime.now().strftime("%d %B %Y")

    # Open file and write information 
    file = open("student_results.txt", "w")

    file.write(f"Student Number: {student_number}\n")
    file.write(f"Student Name: {full_name}\n")
    file.write(f"Course: {course}\n")
    file.write(f"Programming: {programming:.0f}\n")
    file.write(f"Database: {database:.0f}\n")
    file.write(f"Web Development: {web_development:.0f}\n")
    file.write(f"Total: {total:.0f}\n")
    file.write(f"Average: {average:.2f}\n")
    file.write(f"Result: {result}\n")
    file.write(f"Date Saved: {date_saved}\n")

    file.close()

    print("\nResults saved successfully to student_results.txt\n")


def read_results():
    """
    Opens student_results.txt, reads its contents, displays it
    on the console, and closes the file correctly.
    """

    try:
        # ----- Open file and read information -----
        file = open("student_results.txt", "r")

        contents = file.read()

        file.close()

        print("\n----- Student Results -----")
        print(contents)
        print("----------------------------\n")

    except FileNotFoundError:
        print("Error: student_results.txt not found. Please run save_results() first.")


# ----- Main program -----
if __name__ == "__main__":
    save_results()
    read_results()