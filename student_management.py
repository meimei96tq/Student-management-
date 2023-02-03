import display
from prettytable import PrettyTable
student_fields = ['Student ID', 'Student Name', 'Gender', 'Age']

def add_student(conn, cur):
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    global student_fields
    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)
    try:
        cur.execute('INSERT INTO student_k(student_id, name, gender, age) VALUES(%s, %s, %s, %s)',
                    (student_data[0], student_data[1], student_data[2], student_data[3]))
        conn.commit()

        cur.execute('INSERT INTO student_login_k(student_id, student_pass) VALUES(%s, %s)',
                    (student_data[0], '123456'))
        conn.commit()

        print("Data saved successfully")
        input("Press any key to continue")
    except Exception as e:
        print('error', e)
    return


def view_students(conn, cur):
    global student_fields
    print("--- Student Records ---")
    try:
        cur.execute('SELECT * FROM student_k')
    except:
        print('error !')
    data = cur.fetchall()
    t = PrettyTable(student_fields)
    for row in data:
        t.add_row(row)
    print(t)
    input("Press any key to continue")
    return


def search_student(conn, cur):
    global student_fields
    data = []
    display.display_student_search()
    choice = input("Enter your choice: ")
    if choice == '1':
        roll = input("Enter student name to search: ")
        try:
            cur.execute(f'''SELECT * FROM student_k WHERE name ilike '%%{roll}%%' ''')
            data = cur.fetchall()
        except:
            print('error !')
    elif choice == '2':
        roll = input("Enter student id to search: ")
        try:
            cur.execute("SELECT * FROM student_k WHERE student_id = '%s'" % roll)
            data = cur.fetchall()
        except:
            print('error !')
    elif choice == '3':
        roll = input("Enter student gender to search: ")
        try:
            cur.execute("SELECT * FROM student_k WHERE gender == '%s'" % roll)
            data = cur.fetchall()
        except:
            print('error !')

    elif choice == '5':
        roll = input("Enter student age to search: ")
        try:
            cur.execute("SELECT * FROM student_k WHERE age == '%s'" % roll)
            data = cur.fetchall()
        except:
            print('error !')


    if len(data) > 0:
        print("--- Students Found ---")
        t = PrettyTable(student_fields)
        for row in data:
            t.add_row(row)
        print(t)

    else:
        print("No student found in our database")
    input("Press any key to continue")
    return


def update_student(conn, cur):
    update_fields = ['Name', 'Gender', 'Age']
    data = []
    student_data = []
    print("--- Update Student ---")
    roll = input("Enter student id to update: ")
    try:
        cur.execute("SELECT * FROM student_k WHERE student_id = '%s'" % roll)
        data = cur.fetchall()
        if len(data) > 0:
            print("--- Students Found ---")
            t = PrettyTable(student_fields)
            for row in data:
                t.add_row(row)
            print(t)
            print("Enter student information to update")
            for field in update_fields:
                value = input("Enter " + field + ": ")
                student_data.append(value)
            try:
                cur.execute(
                    "UPDATE student_k SET name = '%s', gender = '%s', age = '%s' WHERE student_id = '%s'" % (
                        student_data[0], student_data[1], student_data[2], roll)
                )
                conn.commit()
                print("Data updated successfully")
                input("Press any key to continue")
            except Exception as e:
                print('error', e)
        else:
            print("No student found in our database")
    except Exception as e:
        print('error', e)
    return


def delete_student(conn, cur):
    global student_fields
    print("--- Delete Student ---")
    roll = input("Enter student id to delete: ")
    try:
        cur.execute("SELECT * FROM student_k WHERE student_id = '%s'" % roll)
        data = cur.fetchall()
        if len(data) > 0:
            try:
                cur.execute("DELETE FROM student_k WHERE student_id = '%s'" % roll)
                conn.commit()
                print("Data deleted successfully")
            except Exception as e:
                print('error', e)
        else:
            print("No student found in our database")
    except Exception as e:
        print('error', e)
    input("Press any key to continue")
    return