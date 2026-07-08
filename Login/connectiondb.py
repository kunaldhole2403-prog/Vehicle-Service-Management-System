import mysql.connector

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Kunal@123",
            database="Vehicle_Service_Management"
        )
        return conn

    except mysql.connector.Error as e:
        print("Database Connection Error:", e)
        return None