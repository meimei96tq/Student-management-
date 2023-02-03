import psycopg2
import display, admin, student


def connect():
    # connecting to the database called test
    # using the connect function
    try:
        conn = psycopg2.connect(database="students",
                                user="postgres",
                                password="123456",
                                host="localhost",
                                port="5432")

        # creating the cursor object
        cur = conn.cursor()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while creating PostgreSQL table", error)
    return conn, cur


def admin_management(id):
    conn, cur = connect()
    while True:
        display.display_admin(id)
        choice = input("Enter your choice: ")
        if choice == '1':
            admin.student_management(conn, cur)
        elif choice == '2':
            admin.course_management(conn, cur)
        elif choice == '3':
            admin.grade_management(conn, cur)
        elif choice == '4':
            break
    conn.close()


def admin_login(id, password):
    conn, cur = connect()
    while True:
        try:
            cur.execute("SELECT * FROM admin_login_k WHERE admin_id = '%s' and admin_pass = '%s'" % (id, password))
            data = cur.fetchall()
            if len(data) > 0:
                print("Login successfully!")
                conn.close()
                admin_management(id)
                break
            else:
                print("Id or password incorrect!")
                break
        except Exception as e:
            print('Admin login error !', e)
    return


def student_management(id):
    conn, cur = connect()
    while True:
        display.display_student(id)
        choice = input("Enter your choice: ")
        if choice == '1':
            student.student_info(conn, cur, id)
        elif choice == '2':
            student.course_enrolled_info(conn, cur, id)
        elif choice == '3':
            break
    conn.close()


def student_login(id, password):
    conn, cur = connect()
    while True:
        try:
            cur.execute("SELECT * FROM student_login_k WHERE student_id = '%s' and student_pass = '%s'" % (id, password))
            data = cur.fetchall()
            if len(data) > 0:
                print("Login successfully!")
                conn.close()
                student_management(id)
                break
            else:
                print("Id or password incorrect!")
                break
        except Exception as e:
            print('Student login error !', e)
    return

if __name__ == '__main__':
    while True:
        display.display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            id, password = display.display_login()
            admin_login(id, password)
        elif choice == '2':
            id, password = display.display_login()

        elif choice == '3':
            break
    print("-------------------------------")
    print(" Thank you")
    print("-------------------------------")
