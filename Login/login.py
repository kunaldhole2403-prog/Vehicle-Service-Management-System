from Login.connectiondb import *

def create_user():
    conn = get_connection()

    if conn:
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        email = input("Enter your Email: ")

        cursor = conn.cursor()

        query = """
        INSERT INTO login(username,password,email)
        VALUES(%s,%s,%s)
        """

        cursor.execute(query, (username, password,email))
        conn.commit()

        print("User Created Successfully")

        cursor.close()
        conn.close()

def login():
    conn = get_connection()

    if conn:
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        cursor = conn.cursor()

        query = """
        SELECT * FROM login
        WHERE username=%s AND password=%s
        """

        cursor.execute(query, (username, password))
        data = cursor.fetchone()

        cursor.close()
        conn.close()

        if data:
            print("Login Successful")
            return username
        else:
            print("Invalid Username or Password")
            return None
def change_password(username):

    conn = get_connection()

    if conn:

        cursor = conn.cursor()

        old_password = input("Enter Current Password: ")

        cursor.execute(
            """
            SELECT * FROM login
            WHERE username=%s AND password=%s
            """,
            (username, old_password)
        )

        data = cursor.fetchone()

        if not data:
            print("Incorrect Current Password")
            return

        new_password = input("Enter New Password: ")
        confirm_password = input("Confirm New Password: ")

        if new_password != confirm_password:
            print("Passwords do not match")
            return

        cursor.execute(
            """
            UPDATE login
            SET password=%s
            WHERE username=%s
            """,
            (new_password, username)
        )

        conn.commit()

        print("Password Changed Successfully")

        cursor.close()
        conn.close()