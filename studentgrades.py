def calculate_average(grades):
    return sum(grades) / len(grades)

def get_highest_score(grades):
    return max(grades)

def get_lowest_score(grades):
    return min(grades)

def calculate_grade_distribution(grades):
    distribution = {}
    for grade in grades:
        if grade in distribution:
            distribution[grade] += 1
        else:
            distribution[grade] = 1
    return distribution

# Input number of students
num_students = int(input("Enter the number of students: "))

# Create a list to store student data
students = []

# Input data for each student
for i in range(num_students):
    student = {}
    student["name"] = input(f"Enter student {i+1} name: ")
    num_grades = int(input("Enter the number of grades: "))

    grades = []
    for j in range(num_grades):
        grade = float(input(f"Enter grade {j+1}: "))
        grades.append(grade)

    student["grades"] = grades
    students.append(student)

# Display details of specific student
student_choice = input("Enter the student name or index to display details: ")

for student in students:
    if student_choice == student["name"] or student_choice == str(students.index(student) + 1):
        grades = student["grades"]
        average = calculate_average(grades)
        highest_score = get_highest_score(grades)
        lowest_score = get_lowest_score(grades)
        grade_distribution = calculate_grade_distribution(grades)

        # Display the results for the selected student
        print("\n--- Student Grade Calculator ---")
        print("Student Name:", student["name"])
        print("Grades:", grades)
        print("Average Score:", average)
        print("Highest Score:", highest_score)
        print("Lowest Score:", lowest_score)
        print("Grade Distribution:")
        for grade, count in grade_distribution.items():
            print(f"Grade {grade}: {count} student(s)")
        break
else:
    print("Student not found.")

