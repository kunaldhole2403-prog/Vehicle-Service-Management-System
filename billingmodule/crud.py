from db import conn,cursor

def generate_bill():

    service_id = int(input("Enter Service ID: "))
    amount = float(input("Enter Amount: "))
    payment_status = input("Enter Payment Status (Paid/Pending): ")
    bill_date = input("Enter Bill Date (YYYY-MM-DD): ")

    query = "INSERT INTO Billing(service_id, amount, payment_status, bill_date) VALUES(%s, %s, %s, %s)"

    cursor.execute(query, (service_id, amount, payment_status, bill_date))
    conn.commit()

    print("Bill Generated Successfully!")


def view_bills():

    cursor.execute("SELECT * FROM Billing")
    data = cursor.fetchall()

    for row in data:
        print(row)

def search_bill():

    bill_id = int(input("Enter Bill ID: "))
    cursor.execute("SELECT * FROM Billing WHERE bill_id=%s", (bill_id,))
    data = cursor.fetchone()

    if data:
        print(data)
    else:
        print("Bill Not Found")


def update_payment():

    bill_id = int(input("Enter Bill ID: "))
    status = input("Enter New Status: ")

    cursor.execute("UPDATE Billing SET payment_status=%s WHERE bill_id=%s",(status, bill_id))
    conn.commit()

    print("Updated Successfully")


def delete_bill():

    bill_id = int(input("Enter Bill ID: "))
    cursor.execute("DELETE FROM Billing WHERE bill_id=%s",(bill_id,))
    conn.commit()

    print("Bill Deleted Successfully")
