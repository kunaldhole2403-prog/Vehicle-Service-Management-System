import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kunal@123",
    database="vechicle_service_management"
)

cursor = conn.cursor()

print("Database Connected")