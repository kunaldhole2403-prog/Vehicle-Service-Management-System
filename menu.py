from crud import *

while True:
    print("\n BILLING MENU \n1. Generate Bill\n2. View Bills\n3. Search Bill\n4. Update Payment\n5. Delete Bill\n6. Exit")

    try:
        ch = int(input("Enter choice:"))
        match ch:
            case 1:
                generate_bill()
            case 2:
                view_bills()
            case 3:
                search_bill()
            case 4:
                update_payment()
            case 5:
                delete_bill()
            case 6:
                break
            case _:
                print("Invalid Choice")
    
    except Exception as e:
        print("Enter a numerical value:", e)

        