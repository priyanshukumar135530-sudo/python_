marks = []

def enter_marks():
    global marks
    marks = []
    for i in range(5):
        m = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(m)

def calculate_percentage():
    if not marks:
        print("Enter marks first!")
        return None
    total = sum(marks)
    percentage = total / len(marks)
    return percentage

def assign_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"


while True:
    print("\n--- Student Result System ---")
    print("1. Enter Marks")
    print("2. Calculate Percentage")
    print("3. Assign Grade")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        enter_marks()

    elif choice == '2':
        per = calculate_percentage()
        if per is not None:
            print("Percentage:", per)

    elif choice == '3':
        per = calculate_percentage()
        if per is not None:
            grade = assign_grade(per)
            print("Grade:", grade)

    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid Choice")
