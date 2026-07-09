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
               customer_id int auto_increment primary key,
               customer_name varchar(50) not null,
                phone varchar(15),
                email varchar(50),
                address varchar(100)

               )
  
""" )

conn.commit()
