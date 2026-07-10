import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MYSQL@123",
    database="vehicle_service"
)

cursor = conn.cursor()

print("Database Connected")