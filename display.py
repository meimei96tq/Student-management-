def display_menu():
    print("-------------------------------------")
    print(" Welcome to Student Management System")
    print("-------------------------------------")
    print("1. Login as administrator")
    print("2. Login as student")
    print("3. Quit")

def display_admin(id):
    print("-------------------------------------")
    print(" Welcome ", id)
    print("-------------------------------------")
    print("1. Student management")
    print("2. Course management")
    print("3. Grade management")
    print("4. Log out")

def display_login():
    print("-------------------------------------")
    print(" Login")
    print("-------------------------------------")
    id = input("Enter your id: ")
    password = input("Enter your password: ")
    return id, password

def display_student_managent():
    print("-------------------------------------")
    print("--- Student Management ---")
    print("-------------------------------------")
    print("1. Add New Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Quit")

def display_student_search():
    print("-------------------------------------")
    print("--- Search Student ---")
    print("-------------------------------------")
    print("1. Search by name")
    print("2. Search by student id")
    print("3. Search by gender")
    print("5. Search by age")

def display_course_managent():
    print("-------------------------------------")
    print("--- Course Management ---")
    print("-------------------------------------")
    print("1. Add New Course")
    print("2. View Course")
    print("3. Search Course")
    print("4. Update Course")
    print("5. Delete Course")
    print("6. Quit")

def display_course_search():
    print("-------------------------------------")
    print("--- Search Course ---")
    print("-------------------------------------")
    print("1. Search by name")
    print("2. Search by course id")

def display_grade_management():
    print("-------------------------------------")
    print("--- Grade Management ---")
    print("-------------------------------------")
    print("1. View Student Grade Report")
    print("2. Update Student Grade")
    print("3. Quit")

def display_student_grade_report():
    print("-------------------------------------")
    print("--- View Student Grade Report ---")
    print("-------------------------------------")
    print("1. View by Student")
    print("2. View by Course")

def display_student(id):
    print("-------------------------------------")
    print(" Welcome ", id)
    print("-------------------------------------")
    print("1. View Student Information")
    print("2. View Course Information")
    print("3. Log out")
