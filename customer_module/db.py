import mysql.connector 

# conn create
conn=mysql.connector.connect(
    host=" localhost",
    user="root",
    password="Priya@123",
    database="vehicle_service"
    )
print(" database connected !")




# table creation
cursor=conn.cursor()
cursor.execute("""
  create table if not exists customer(
               customer_id INT AUTO_INCREMENT PRIMARY KEY,
               customer_name VARCHAR(50) NOT NULL,
                phone VARCHAR(15),
                email VARCHAR(50),
                address VARCHAR(100)

               )
  
""" )

conn.commit()
print(" table created !")
