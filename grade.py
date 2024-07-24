"""
Program that stores and manages details about a student:
    Department, Course, Number of units done, score for each unit, average score
Note that grade is based on the average score from 90-100(A), from 80-89(B), from 70-79(C)
60-69(D). then 0-59(FAIL)
"""


student_records = {}

def calculate_average_and_grade(scores):
    if not scores:
        return 0, 'FAIL'
    average = sum(scores) / len(scores)
    if 90 <= average <= 100:
        grade = 'A'
    elif 80 <= average <= 89:
        grade = 'B'
    elif 70 <= average <= 79:
        grade = 'C'
    elif 60 <= average <= 69:
        grade = 'D'
    else:
        grade = 'FAIL'
    return average, grade

def add_student():
    name = input("Please enter your name: ")
    reg_no = input("Please enter reg no: ")
    department = input("Enter your department: ")
    course = input("Enter the student's course: ")

    num_units = int(input("Enter number of units: "))
    scores = []
    for i in range(num_units):
        score = float(input(f"Enter score for unit {i + 1}: "))
        scores.append(score)

    average, grade = calculate_average_and_grade(scores)

    student_records[reg_no] = {
        'name': name,
        'department': department,
        'course': course,
        'scores': scores,
        'average_score': average,
        'grade': grade
    }

    print(f"Student records added successfully!")

def display_student_record(reg_no):
    if reg_no in student_records:
        records = student_records[reg_no]
        print(f"Name: {records[ 'name' ]}")
        print(f"Average score {records[ 'average_score' ]:.2F}")
        print(f"Course: {records[ 'course' ]}")
        print(f"Scores: {records[ 'scores' ]}")
        print(f"Department: {records[ 'department' ]}")
    else:
        print(f"Students with registration number {reg_no} not found")

def update_student_record(reg_no):
    if reg_no in student_records:
        print("Update record for: ", reg_no)
        print("Leave if you want to skip option")
        name = input(f"Enter your preferred new name (current: {student_records[reg_no]['name']}): ")
        course = input(f"Enter your preferred new course (current: {student_records[reg_no]['course']}): ")

        if name:
            student_records[reg_no][name] = name
        if course:
            student_records[reg_no][course] = course

    else:
        print(f"Student record not found")

def delete_student(reg_no):
    if reg_no in student_records:
        del student_records[reg_no]
        print("Student record deleted successfully.")
    else:
        print("Student not found")

#search a student by name
def search_student(name):
    Found = False
    for reg_no, record in student_records.items():
        if record['name'].lower() == name.lower():
            display_student_record(reg_no)
            found = True
            break #Exit the loop once the student is found
        if not found:
            print("Student not found!")

def menu():
    while True:
        print("\nStudent records system")
        print("1. Add student ")
        print("2. Display student ")
        print("3. Update student record")
        print("4. Delete a student ")
        print("5. Search for Student ")
        print("6. Exit system")

        choice = input("Enter your preferred choice: ")

        if choice == '1':
            add_student()
        elif choice == 2:
            reg_no = input("Enter registration number to display")
            display_student_record(reg_no)
        elif choice == '3':
            reg_no = input("Enter registration number to display")
            update_student_record(reg_no)
        elif choice == '4':
            reg_no = input("Enter registration number to delete")
            delete_student(reg_no)
        elif choice == '5':
            name = input("Enter the name of the student to search")
            search_student(name)
        elif choice == '6':
            print("Exiting...please wait")
            break
        else:
            print("Error: Invalid choice, please try again!")

if __name__ == "__main__":
    menu()