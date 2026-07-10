import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kunal@123"
    )
    cursor = conn.cursor()

    print("Connected Successfully")

except Exception as e:
    print("Error:", e)