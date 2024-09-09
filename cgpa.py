def cgpa_calculator():
    print("CGPA Calculator")

    num_courses = int(input("Enter the number of courses: "))
    total_points = 0
    total_credits = 0

    for _ in range(num_courses):
        grade = float(input("Enter the grade for the course: "))
        credits = float(input("Enter the credit hours for the course: "))
        total_points += grade * credits
        total_credits += credits

    if total_credits == 0:
        print("Error: Total credits cannot be zero.")
    else:
        cgpa = total_points / total_credits
        print(f"Your CGPA is: {cgpa:.2f}")

cgpa_calculator()
