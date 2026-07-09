import mysql.connector

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Kunal@123",
            database="vechicle_service_management"
        )
        return conn

    except mysql.connector.Error as e:
        print("Database Connection Error:", e)
        return None