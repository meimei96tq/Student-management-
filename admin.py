import display
import student_management as sm
import course_management as cm
import grade_management as gm

def student_management(conn, cur):
    while True:
        display.display_student_managent()
        choice = input("Enter your choice: ")
        if choice == '1':
            sm.add_student(conn, cur)
        elif choice == '2':
            sm.view_students(conn, cur)
        elif choice == '3':
            sm.search_student(conn, cur)
        elif choice == '4':
            sm.update_student(conn, cur)
        elif choice == '5':
            sm.delete_student(conn, cur)
        elif choice == '6':
            break
    return
def course_management(conn, cur):
    while True:
        display.display_course_managent()
        choice = input("Enter your choice: ")
        if choice == '1':
            cm.add_course(conn, cur)
        elif choice == '2':
            cm.view_course(conn, cur)
        elif choice == '3':
            cm.search_course(conn, cur)
        elif choice == '4':
            cm.update_course(conn, cur)
        elif choice == '5':
            cm.delete_course(conn, cur)
        elif choice == '6':
            break
    return
def grade_management(conn, cur):
    while True:
        display.display_grade_management()
        choice = input("Enter your choice: ")
        if choice == '1':
            gm.view_grade(conn, cur)
        elif choice == '2':
            gm.update_grade(conn, cur)
        elif choice == '3':
            break
    return


