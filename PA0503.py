def get_student_age():
    #Handle letters instead of an age
    try:
        age = int(input("Enter student age: "))
    except ValueError:
        print("Error: Age must be a whole number.")
        return None
    else:
        print(f"Age accepted: {age}")
        return age
    finally:
        print("Done checking age.\n")


def get_student_mark():
    #Handle letters instead of a mark, and marks outside 0-100
    try:
        mark = float(input("Enter mark (0-100): "))
        if mark < 0 or mark > 100:
            print("Error: Mark must be between 0 and 100.")
            return None
    except ValueError:
        print("Error: Mark must be a number.")
        return None
    else:
        print(f"Mark accepted: {mark}")
        return mark
    finally:
        print("Done checking mark.\n")


def calculate_average(marks):
    #Handle division by zero
    try:
        average = sum(marks) / len(marks)
    except ZeroDivisionError:
        print("Error: Cannot calculate average - no marks provided.")
        return None
    else:
        print(f"Average calculated: {round(average, 2)}")
        return average
    finally:
        print("Done calculating average.\n")


def add_student():
    name = input("Enter new student name: ").strip()
    age = get_student_age()
    mark1 = get_student_mark()
    mark2 = get_student_mark()
    mark3 = get_student_mark()

    marks = [m for m in [mark1, mark2, mark3] if m is not None]
    average = calculate_average(marks)

    if average is not None:
        print(f"{name} added with average: {round(average, 2)}")
    else:
        print(f"{name} could not be added - incomplete or invalid data.")


# Running it
add_student()