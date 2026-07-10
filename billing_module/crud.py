from billing_module.db import conn, cursor

GST_RATE = 0.18

SERVICE_PRICES = {
    "Oil Change": 500.00,
    "Car Wash": 300.00,
    "Battery Check": 200.00,
    
}

def generate_bill():
    try:
        service_id = int(input("Enter Service ID: "))
        payment_status = input("Enter Payment Status (Paid/Pending): ")
        bill_date = input("Enter Bill Date (YYYY-MM-DD): ")

        cursor.execute("SELECT vehicle_id, service_type FROM Service WHERE service_id=%s", (service_id,))
        service = cursor.fetchone()

        if not service:
            print("No such service found.")
            return

        vehicle_id, service_type = service
        price = SERVICE_PRICES.get(service_type)

        if price is None:
            print(f"No price set for '{service_type}'.")
            return

        gst_amount = price * GST_RATE
        total_amount = price + gst_amount

        cursor.execute(
            "INSERT INTO Billing (service_id, amount, payment_status, bill_date) VALUES (%s, %s, %s, %s)",
            (service_id, total_amount, payment_status, bill_date)
        )
        conn.commit()
        bill_id = cursor.lastrowid

        cursor.execute("SELECT vehicle_no FROM Vehicle WHERE vehicle_id=%s", (vehicle_id,))
        vehicle_no = cursor.fetchone()[0]

        print("\n" + "=" * 40)
        print(f"Bill ID: {bill_id} | Vehicle: {vehicle_no}")
        print(f"{service_type:20}₹{price:>8.2f}")
        print(f"GST(18%):{'':11}₹{gst_amount:>8.2f}")
        print(f"Total:{'':14}₹{total_amount:>8.2f}")
        print(f"Status: {payment_status} | Date: {bill_date}")
        print("=" * 40)

    except Exception as e:
        print("Error generating bill:", e)


def view_bills():
    try:
        print("\n1. View by Vehicle ID")
        print("2. View by Customer ID")
        choice = input("Enter choice: ")

        if choice == "1":
            vehicle_id = int(input("Enter Vehicle ID: "))
            query = """
                SELECT b.bill_id, v.vehicle_no, s.service_type,
                       b.amount, b.payment_status, b.bill_date
                FROM Billing b
                JOIN Service s ON b.service_id = s.service_id
                JOIN Vehicle v ON s.vehicle_id = v.vehicle_id
                WHERE v.vehicle_id = %s
                ORDER BY b.bill_date DESC
            """
            cursor.execute(query, (vehicle_id,))

        elif choice == "2":
            customer_id = int(input("Enter Customer ID: "))
            query = """
                SELECT b.bill_id, v.vehicle_no, s.service_type,
                       b.amount, b.payment_status, b.bill_date
                FROM Billing b
                JOIN Service s ON b.service_id = s.service_id
                JOIN Vehicle v ON s.vehicle_id = v.vehicle_id
                JOIN Customer c ON v.customer_id = c.customer_id
                WHERE c.customer_id = %s
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

        print("\n" + "=" * 70)
        print(f"{'Bill ID':<10}{'Vehicle No':<15}{'Service':<18}{'Amount':>10}{'Status':>10}{'Date':>12}")
        print("-" * 70)
        for bill_id, vehicle_no, service_type, amount, status, bill_date in bills:
            print(f"{bill_id:<10}{vehicle_no:<15}{service_type:<18}₹{amount:>8.2f}{status:>10}{str(bill_date):>12}")
        print("=" * 70)

    except Exception as e:
        print("Error fetching bills:", e)

def search_bill():
    try:
        bill_id = int(input("Enter Bill ID: "))
        vehicle_no = input("Enter Vehicle No: ").strip()

        query = """
            SELECT b.bill_id, v.vehicle_no, s.service_type,
                   b.amount, b.payment_status, b.bill_date
            FROM Billing b
            JOIN Service s ON b.service_id = s.service_id
            JOIN Vehicle v ON s.vehicle_id = v.vehicle_id
            WHERE b.bill_id = %s AND v.vehicle_no = %s
        """
        cursor.execute(query, (bill_id, vehicle_no))
        data = cursor.fetchone()

        if not data:
            print("Bill not found.")
            return

        bill_id, vehicle_no, service_type, amount, status, bill_date = data

        print("\n------- BILL -------")
        print(f"Bill ID   : {bill_id}")
        print(f"Vehicle   : {vehicle_no}")
        print(f"Service   : {service_type}")
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

        cursor.execute(
            """SELECT b.bill_id, v.vehicle_no, s.service_type, b.amount, b.payment_status, b.bill_date
               FROM Billing b
               JOIN Service s ON b.service_id = s.service_id
               JOIN Vehicle v ON s.vehicle_id = v.vehicle_id
               WHERE b.bill_id = %s""",
            (bill_id,)
        )
        bill = cursor.fetchone()

        if not bill:
            print("No bill found with that Bill ID.")
            return

        bill_id, vehicle_no, service_type, amount, status, bill_date = bill

        print("\nYou are about to delete this bill:")
        print(f"Bill ID   : {bill_id}")
        print(f"Vehicle   : {vehicle_no}")
        print(f"Service   : {service_type}")
        print(f"Amount    : ₹{amount:.2f}")
        print(f"Status    : {status}")
        print(f"Date      : {bill_date}")

        confirm = input("\nType 'yes' to confirm deletion: ").strip().lower()

        if confirm != "yes":
            print("Deletion cancelled.")
            return

        cursor.execute("DELETE FROM Billing WHERE bill_id=%s", (bill_id,))
        conn.commit()

        print("Bill Deleted Successfully")

    except Exception as e:
        print("Error deleting bill:", e)