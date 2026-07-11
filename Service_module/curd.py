from Service_module.db import conn, cursor


def add_service():

    try:
        vehicle_id = int(input("Enter Vehicle ID: "))
        service_date = input("Enter Service Date (YYYY-MM-DD): ")
        status = input("Enter Status (Pending/Completed): ")

        cursor.execute("""
            INSERT INTO Service_Record
            (vehicle_id, service_date, status)
            VALUES (%s,%s,%s)
        """, (vehicle_id, service_date, status))

        conn.commit()

        service_id = cursor.lastrowid

        print("\nAvailable Services")

        cursor.execute("SELECT * FROM Service_Master")

        services = cursor.fetchall()

        for sid, name, price in services:
            print(f"{sid}. {name} - ₹{price}")

        selected = input(
            "\nEnter Service IDs separated by comma (1,2,3): "
        )

        service_ids = selected.split(",")

        for sm_id in service_ids:

            cursor.execute("""
                INSERT INTO Service_Details
                (service_id, service_master_id)
                VALUES (%s,%s)
            """, (service_id, int(sm_id.strip())))

        conn.commit()

        print("Service Added Successfully")

    except Exception as e:
        print("Error:", e)


def view_services():

    try:

        query = """
        SELECT sr.service_id,
               v.vehicle_no,
               sr.service_date,
               sr.status
        FROM Service_Record sr
        JOIN Vehicle v
        ON sr.vehicle_id = v.vehicle_id
        """

        cursor.execute(query)

        records = cursor.fetchall()

        if not records:
            print("No Service Records Found")
            return

        print("\n" + "=" * 70)

        for service_id, vehicle_no, date, status in records:

            cursor.execute("""
                SELECT sm.service_name
                FROM Service_Details sd
                JOIN Service_Master sm
                ON sd.service_master_id = sm.service_master_id
                WHERE sd.service_id=%s
            """, (service_id,))

            services = [row[0] for row in cursor.fetchall()]

            print(f"Service ID : {service_id}")
            print(f"Vehicle No : {vehicle_no}")
            print(f"Services   : {', '.join(services)}")
            print(f"Date       : {date}")
            print(f"Status     : {status}")
            print("-" * 70)

    except Exception as e:
        print("Error:", e)


def search_service():

    try:

        service_id = int(input("Enter Service ID: "))

        query = """
        SELECT sr.service_id,
               v.vehicle_no,
               sr.service_date,
               sr.status
        FROM Service_Record sr
        JOIN Vehicle v
        ON sr.vehicle_id = v.vehicle_id
        WHERE sr.service_id=%s
        """

        cursor.execute(query, (service_id,))

        data = cursor.fetchone()

        if not data:
            print("Service Not Found")
            return

        service_id, vehicle_no, date, status = data

        cursor.execute("""
            SELECT sm.service_name,
                   sm.price
            FROM Service_Details sd
            JOIN Service_Master sm
            ON sd.service_master_id = sm.service_master_id
            WHERE sd.service_id=%s
        """, (service_id,))

        services = cursor.fetchall()

        print("\n===== SERVICE DETAILS =====")
        print(f"Service ID : {service_id}")
        print(f"Vehicle No : {vehicle_no}")
        print(f"Date       : {date}")
        print(f"Status     : {status}")

        print("\nSelected Services")

        total = 0

        for name, price in services:
            print(f"{name} - ₹{price}")
            total += float(price)

        print(f"\nTotal Cost : ₹{total}")

    except Exception as e:
        print("Error:", e)


def update_service():

    try:

        service_id = int(input("Enter Service ID: "))
        status = input("Enter New Status: ")

        cursor.execute("""
            UPDATE Service_Record
            SET status=%s
            WHERE service_id=%s
        """, (status, service_id))

        conn.commit()

        print("Service Updated Successfully")

    except Exception as e:
        print("Error:", e)


def delete_service():

    try:

        service_id = int(input("Enter Service ID: "))

        cursor.execute("""
            SELECT service_id
            FROM Service_Record
            WHERE service_id=%s
        """, (service_id,))

        if not cursor.fetchone():
            print("Service Not Found")
            return

        confirm = input(
            "Type YES to delete service: "
        ).upper()

        if confirm != "YES":
            print("Deletion Cancelled")
            return

        cursor.execute(
            "DELETE FROM Service_Details WHERE service_id=%s",
            (service_id,)
        )

        cursor.execute(
            "DELETE FROM Service_Record WHERE service_id=%s",
            (service_id,)
        )

        conn.commit()

        print("Service Deleted Successfully")

    except Exception as e:
        print("Error:", e)