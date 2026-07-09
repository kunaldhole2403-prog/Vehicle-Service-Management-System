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
            return True
        else:
            print("Invalid Username or Password")
            return False
