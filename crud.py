from db import conn, cursor

def add():
    customer_id = input("Customer ID : ")
    vehicle_no = input("Vehicle Number : ")
    company = input("Company : ")

    sql = "INSERT INTO Vehicle(customer_id,vehicle_no,company) VALUES(%s,%s,%s)"
    cursor.execute(sql, (customer_id, vehicle_no, company))
    conn.commit()

    print("Vehicle Added")


def view():
    cursor.execute("SELECT * FROM Vehicle")
    data = cursor.fetchall()

    for row in data:
        print(row)


def search():
    vehicle_no = input("Vehicle Number : ")

    sql = "SELECT * FROM Vehicle WHERE vehicle_no=%s"
    cursor.execute(sql, (vehicle_no,))

    row = cursor.fetchone()

    if row:
        print(row)
    else:
        print("Vehicle Not Found")


def update():
    vehicle_no = input("Vehicle Number : ")
    company = input("New Company : ")

    sql = "UPDATE Vehicle SET company=%s WHERE vehicle_no=%s"
    cursor.execute(sql, (company, vehicle_no))
    conn.commit()

    print("Vehicle Updated")


def delete():
    vehicle_no = input("Vehicle Number : ")

    sql = "DELETE FROM Vehicle WHERE vehicle_no=%s"
    cursor.execute(sql, (vehicle_no,))
    conn.commit()

    print("Vehicle Deleted")