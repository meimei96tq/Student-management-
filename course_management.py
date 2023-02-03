import display
from prettytable import PrettyTable
course_fields = ['CourseID', 'Course Name', 'Credit']

def add_course(conn, cur):
    print("-------------------------")
    print("Add Course Information")
    print("-------------------------")
    global course_fields
    course_data = []
    for field in course_fields:
        value = input("Enter " + field + ": ")
        course_data.append(value)
    try:
        cur.execute('INSERT INTO course_k(course_id, course_name, credit) VALUES(%s, %s, %s)',
                    (course_data[0], course_data[1], course_data[2]))
        conn.commit()
        print("Data saved successfully")
        input("Press any key to continue")
    except Exception as e:
        print('error', e)
    return


def view_course(conn, cur):
    global course_fields
    print("--- Course Records ---")
    try:
        cur.execute('SELECT * FROM course_k')
    except:
        print('error !')
    data = cur.fetchall()
    t = PrettyTable(course_fields)
    for row in data:
        t.add_row(row)
    print(t)
    input("Press any key to continue")
    return


def search_course(conn, cur):
    global course_fields
    data = []
    display.display_course_search()
    choice = input("Enter your choice: ")
    if choice == '1':
        roll = input("Enter course name to search: ")
        try:
            cur.execute(f'''SELECT * FROM course_k WHERE course_name ilike '%%{roll}%%' ''')
            data = cur.fetchall()
        except:
            print('error !')
    elif choice == '2':
        roll = input("Enter course id to search: ")
        try:
            cur.execute("SELECT * FROM course_k WHERE course_id = '%s'" % roll)
            data = cur.fetchall()
        except:
            print('error !')

    if len(data) > 0:
        print("--- Course Found ---")
        t = PrettyTable(course_fields)
        for row in data:
            t.add_row(row)
        print(t)
    else:
        print("No course found in our database")
    input("Press any key to continue")
    return


def update_course(conn, cur):
    global course_fields
    update_fields = ['Course Name', 'Credit']
    data = []
    course_data = []
    print("--- Update Course ---")
    roll = input("Enter course id to update: ")
    try:
        cur.execute("SELECT * FROM course_k WHERE course_id = '%s'" % roll)
        data = cur.fetchall()
        if len(data) > 0:
            print("--- Course Found ---")
            t = PrettyTable(course_fields)
            for row in data:
                t.add_row(row)
            print(t)
            print("Enter course information to update")
            for field in update_fields:
                value = input("Enter " + field + ": ")
                course_data.append(value)
            try:
                cur.execute(
                    "UPDATE course_k SET course_name = '%s', credit = '%s' WHERE course_id = '%s'" % (
                        course_data[0], course_data[1], roll)
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


def delete_course(conn, cur):
    global course_fields
    print("--- Delete Course ---")
    roll = input("Enter course id to delete: ")
    try:
        cur.execute("SELECT * FROM course_k WHERE course_id = '%s'" % roll)
        data = cur.fetchall()
        if len(data) > 0:
            try:
                cur.execute("DELETE FROM course_k WHERE course_k = '%s'" % roll)
                conn.commit()
                print("Data deleted successfully")
            except Exception as e:
                print('error', e)
        else:
            print("No course found in our database")
    except Exception as e:
        print('error', e)
    input("Press any key to continue")
    return