import mysql.connector as x

conn = x.connect(
    host="localhost",
    user="root",
    password="Mohini@08",
    database="vms",
    use_pure=True
)

cursor = conn.cursor()
print("Database Connected")