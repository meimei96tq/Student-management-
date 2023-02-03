import display
from prettytable import PrettyTable

student_fields = ['Student ID', 'Student Name', 'Gender', 'Age']


def student_info(conn, cur, id):
    data = []
    print("-------------------------------------")
    print("--- Student Information ---")
    print("-------------------------------------")
    try:
        cur.execute("SELECT * FROM student_k WHERE student_id = '%s'" % id)
        data = cur.fetchall()
    except:
        print('error !')
    t = PrettyTable(student_fields)
    for row in data:
        t.add_row(row)
    print(t)
    input("Press any key to continue")
    return


def course_enrolled_info(conn, cur, id):
    course_fields = ["Course id", "Course name", "Credit", "Score", "Status"]
    data = []
    print("-------------------------------------")
    print("--- Course Enrolled Information ---")
    print("-------------------------------------")
    try:
        cur.execute(
            "SELECT course_k.course_id, course_k.course_name, course_k.credit, grade_k.score, grade_k.status \
            FROM grade_k \
            INNER JOIN student_k ON student_k.student_id = grade_k.student_id \
            INNER JOIN course_k ON course_k.course_id = grade_k.course_id \
            WHERE student_k.student_id = '%s'" % id)
        data = cur.fetchall()
    except:
        print('error !')
    t = PrettyTable(course_fields)
    for row in data:
        t.add_row(row)
    print(t)
    input("Press any key to continue")
    return

