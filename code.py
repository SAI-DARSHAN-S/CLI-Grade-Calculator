def get_grade(percentage):
    if percentage >= 80:
        return "A"
    elif percentage >= 65:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


def enter_marks():
    marks = {}

    while True:
        try:
            number = int(input("Enter number of subjects: "))

            if number > 0:
                break

            print("Enter a number greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

    for i in range(number):
        subject = input(f"Enter subject {i + 1} name: ").strip()

        while subject == "":
            print("Subject name cannot be empty.")
            subject = input(f"Enter subject {i + 1} name: ").strip()

        while True:
            try:
                mark = float(input(f"Enter marks for {subject}: "))

                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break

                print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid mark.")

    return marks


def calculate_result(marks):
    total = sum(marks.values())
    percentage = total / len(marks)
    grade = get_grade(percentage)

    return total, percentage, grade


def display_result(name, marks):
    total, percentage, grade = calculate_result(marks)

    print("\n" + "=" * 40)
    print("           GRADE REPORT")
    print("=" * 40)
    print("Student Name:", name)

    print("\nSubject Marks:")
    for subject, mark in marks.items():
        print(f"{subject:<25} {mark:g}")

    print("-" * 40)
    print(f"Total      : {total:g}")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Grade      : {grade}")

    if percentage >= 40:
        print("Result     : PASS")
    else:
        print("Result     : FAIL")

    print("=" * 40)


def main():
    while True:
        print("\n===== CLI GRADE CALCULATOR =====")
        print("1. Calculate Grade")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("\nEnter student name: ").strip()

            if name == "":
                print("Student name cannot be empty.")
                continue

            marks = enter_marks()
            display_result(name, marks)

        elif choice == "2":
            print("\nThank you for using the Grade Calculator!")
            break

        else:
            print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()