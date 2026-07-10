import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kunal@123",
        database="vechicle_service_management"
    )

    cursor = conn.cursor()

except Exception as e:
    print("Error:", e)