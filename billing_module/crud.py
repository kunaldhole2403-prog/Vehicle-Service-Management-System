from billing_module.db import conn, cursor

GST_RATE = 0.18

def generate_bill():
    try:
        service_id = int(input("Enter Service ID: "))
        payment_status = input("Enter Payment Status (Paid/Pending): ")
        bill_date = input("Enter Bill Date (YYYY-MM-DD): ")

        cursor.execute("""
            SELECT sr.vehicle_id,
                   sm.service_name,
                   sm.price
            FROM Service_Details sd
            JOIN Service_Master sm
                 ON sd.service_master_id = sm.service_master_id
            JOIN Service_Record sr
                 ON sd.service_id = sr.service_id
            WHERE sd.service_id = %s
        """, (service_id,))

        services = cursor.fetchall()

        if not services:
            print("No services found.")
            return

        vehicle_id = services[0][0]

        subtotal = 0

        print("\nSelected Services")
        print("-" * 35)

        for _, service_name, price in services:
            print(f"{service_name:<20} ₹{price:.2f}")
            subtotal += float(price)

        gst_amount = subtotal * GST_RATE
        total_amount = subtotal + gst_amount

        cursor.execute("""
            INSERT INTO Billing
            (service_id, amount, payment_status, bill_date)
            VALUES (%s,%s,%s,%s)
        """, (service_id, total_amount,
              payment_status, bill_date))

        conn.commit()

        bill_id = cursor.lastrowid

        cursor.execute(
            "SELECT vehicle_no FROM Vehicle WHERE vehicle_id=%s",
            (vehicle_id,)
        )

        vehicle_no = cursor.fetchone()[0]

        print("\n" + "=" * 40)
        print(f"Bill ID : {bill_id}")
        print(f"Vehicle : {vehicle_no}")
        print("-" * 40)
        print(f"Subtotal : ₹{subtotal:.2f}")
        print(f"GST 18%  : ₹{gst_amount:.2f}")
        print(f"Total    : ₹{total_amount:.2f}")
        print("=" * 40)

    except Exception as e:
        print("Error:", e)

def view_bills():
    try:
        print("\n1. View by Vehicle ID")
        print("2. View by Customer ID")
        choice = input("Enter choice: ")

        if choice == "1":
            vehicle_id = int(input("Enter Vehicle ID: "))

            query = """
                SELECT b.bill_id,
                       v.vehicle_no,
                       b.amount,
                       b.payment_status,
                       b.bill_date,
                       b.service_id
                FROM Billing b
                JOIN Service_Record sr
                    ON b.service_id = sr.service_id
                JOIN Vehicle v
                    ON sr.vehicle_id = v.vehicle_id
                WHERE v.vehicle_id = %s
                ORDER BY b.bill_date DESC
            """
            cursor.execute(query, (vehicle_id,))

        elif choice == "2":
            customer_id = int(input("Enter Customer ID: "))

            query = """
                SELECT b.bill_id,
                       v.vehicle_no,
                       b.amount,
                       b.payment_status,
                       b.bill_date,
                       b.service_id
                FROM Billing b
                JOIN Service_Record sr
                    ON b.service_id = sr.service_id
                JOIN Vehicle v
                    ON sr.vehicle_id = v.vehicle_id
                WHERE v.customer_id = %s
                ORDER BY b.bill_date DESC
            """
            cursor.execute(query, (customer_id,))

        else:
            print("Invalid choice.")
            return

        bills = cursor.fetchall()

        if not bills:
            print("No bills found.")
            return

        print("\n" + "=" * 90)

        for bill_id, vehicle_no, amount, status, bill_date, service_id in bills:

            cursor.execute("""
                SELECT sm.service_name
                FROM Service_Details sd
                JOIN Service_Master sm
                    ON sd.service_master_id = sm.service_master_id
                WHERE sd.service_id = %s
            """, (service_id,))

            services = [row[0] for row in cursor.fetchall()]

            print(f"Bill ID    : {bill_id}")
            print(f"Vehicle No : {vehicle_no}")
            print(f"Services   : {', '.join(services)}")
            print(f"Amount     : ₹{amount:.2f}")
            print(f"Status     : {status}")
            print(f"Date       : {bill_date}")
            print("-" * 90)

    except Exception as e:
        print("Error fetching bills:", e)
def search_bill():
    try:
        bill_id = int(input("Enter Bill ID: "))
        vehicle_no = input("Enter Vehicle No: ").strip()

        query = """
            SELECT b.bill_id,
                   v.vehicle_no,
                   b.amount,
                   b.payment_status,
                   b.bill_date,
                   b.service_id
            FROM Billing b
            JOIN Service_Record sr
                ON b.service_id = sr.service_id
            JOIN Vehicle v
                ON sr.vehicle_id = v.vehicle_id
            WHERE b.bill_id = %s
            AND v.vehicle_no = %s
        """

        cursor.execute(query, (bill_id, vehicle_no))
        data = cursor.fetchone()

        if not data:
            print("Bill not found.")
            return

        bill_id, vehicle_no, amount, status, bill_date, service_id = data

        cursor.execute("""
            SELECT sm.service_name
            FROM Service_Details sd
            JOIN Service_Master sm
                ON sd.service_master_id = sm.service_master_id
            WHERE sd.service_id = %s
        """, (service_id,))

        services = [row[0] for row in cursor.fetchall()]

        print("\n------- BILL -------")
        print(f"Bill ID   : {bill_id}")
        print(f"Vehicle   : {vehicle_no}")
        print(f"Services  : {', '.join(services)}")
        print(f"Amount    : ₹{amount:.2f}")
        print(f"Status    : {status}")
        print(f"Date      : {bill_date}")
        print("--------------------")

    except Exception as e:
        print("Error:", e)

def update_payment():
    try:
        bill_id = int(input("Enter Bill ID: "))
        status = input("Enter New Status (Paid/Pending): ").strip().capitalize()

        if status not in ("Paid", "Pending"):
            print("Invalid status. Use 'Paid' or 'Pending'.")
            return

        cursor.execute("SELECT bill_id FROM Billing WHERE bill_id=%s", (bill_id,))
        if not cursor.fetchone():
            print("No bill found with that Bill ID.")
            return

        cursor.execute(
            "UPDATE Billing SET payment_status=%s WHERE bill_id=%s",
            (status, bill_id)
        )
        conn.commit()

        print("Payment Status Updated Successfully")

    except Exception as e:
        print("Error updating payment:", e)


def delete_bill():
    try:
        bill_id = int(input("Enter Bill ID: "))

        query = """
            SELECT b.bill_id,
                   v.vehicle_no,
                   b.amount,
                   b.payment_status,
                   b.bill_date,
                   b.service_id
            FROM Billing b
            JOIN Service_Record sr
                ON b.service_id = sr.service_id
            JOIN Vehicle v
                ON sr.vehicle_id = v.vehicle_id
            WHERE b.bill_id = %s
        """

        cursor.execute(query, (bill_id,))
        bill = cursor.fetchone()

        if not bill:
            print("No bill found.")
            return

        bill_id, vehicle_no, amount, status, bill_date, service_id = bill

        cursor.execute("""
            SELECT sm.service_name
            FROM Service_Details sd
            JOIN Service_Master sm
                ON sd.service_master_id = sm.service_master_id
            WHERE sd.service_id = %s
        """, (service_id,))

        services = [row[0] for row in cursor.fetchall()]

        print("\nYou are about to delete:")
        print(f"Bill ID   : {bill_id}")
        print(f"Vehicle   : {vehicle_no}")
        print(f"Services  : {', '.join(services)}")
        print(f"Amount    : ₹{amount:.2f}")
        print(f"Status    : {status}")
        print(f"Date      : {bill_date}")

        confirm = input("\nType 'yes' to confirm deletion: ").strip().lower()

        if confirm != "yes":
            print("Deletion Cancelled")
            return

        cursor.execute(
            "DELETE FROM Billing WHERE bill_id=%s",
            (bill_id,)
        )

        conn.commit()

        print("Bill Deleted Successfully")

    except Exception as e:
        print("Error deleting bill:", e)