import display
from prettytable import PrettyTable
grade_fields = ["StudentID", "Student Name", "CourseID", "Course Name", "Score", "Status"]


def view_grade(conn, cur):
    display.display_student_grade_report()
    choice = input("Enter your choice: ")
    grade_fields = []
    if choice == '1':
        grade_fields = ["Course id", "Course name", "Score", "Status"]
        roll = input("Enter student id to search: ")
        try:
            cur.execute(
                "SELECT student_k.name, course_k.course_id, course_k.course_name, grade_k.score, grade_k.status \
                FROM grade_k \
                INNER JOIN student_k ON student_k.student_id = grade_k.student_id \
                INNER JOIN course_k ON course_k.course_id = grade_k.course_id \
                WHERE student_k.student_id = '%s'" % roll)
            data = cur.fetchall()
        except:
            print('error !')
    elif choice == '2':
        grade_fields = ["StudentID", "Student Name", "Score", "Status"]
        roll = input("Enter course id to search: ")
        try:
            cur.execute(
                "SELECT course_k.course_name, student_k.student_id, student_k.name, grade_k.score, grade_k.status \
                FROM grade_k \
                INNER JOIN student_k ON student_k.student_id = grade_k.student_id \
                INNER JOIN course_k ON course_k.course_id = grade_k.course_id \
                WHERE course_k.course_id = '%s'" % roll)
            data = cur.fetchall()
        except:
            print('error !')

    if len(data) > 0:
        if choice == '1':
            print("--- Student Grade report ---")
            print("Student: ", data[0][0], "(", roll, ")")
            t = PrettyTable(grade_fields)
            for row in data:
                t.add_row(row[1:])
            print(t)
        if choice == '2':
            print("--- Student Grade report ---")
            print("Course: ", data[0][0], "(", roll, ")")
            t = PrettyTable(grade_fields)
            for row in data:
                t.add_row(row[1:])
            print(t)

    else:
        print("No course found in our database")
    input("Press any key to continue")
    return

def update_grade(conn, cur):
    global grade_fields
    update_fields = ["Score", "Status"]
    grade_data = []
    print("--- Update Grade ---")
    print("Enter course id and student id to update")
    course_id = input("Enter course id: ")
    student_id = input("Enter student id: ")
    try:
        cur.execute(
            "SELECT student_k.student_id, student_k.name, course_k.course_id, course_k.course_name, grade_k.score, grade_k.status \
            FROM grade_k \
            INNER JOIN student_k ON student_k.student_id = grade_k.student_id \
            INNER JOIN course_k ON course_k.course_id = grade_k.course_id \
            WHERE student_k.student_id = '%s' and course_k.course_id = '%s'" % (student_id, course_id))
        data = cur.fetchall()
        if len(data) > 0:
            print("--- Student Found ---")
            t = PrettyTable(grade_fields)
            for row in data:
                t.add_row(row)
            print(t)
            print("Enter grade information to update")
            for field in update_fields:
                value = input("Enter " + field + ": ")
                grade_data.append(value)
            try:
                cur.execute(
                    "UPDATE grade_k SET score = '%s', status = '%s' WHERE student_id = '%s' and course_id = '%s'" % (
                        grade_data[0], grade_data[1], student_id, course_id)
                )
                conn.commit()
                print("Data updated successfully")
                input("Press any key to continue")
            except Exception as e:
                print('error', e)
        else:
            print("No course found in our database")
    except Exception as e:
        print('error', e)
    return
