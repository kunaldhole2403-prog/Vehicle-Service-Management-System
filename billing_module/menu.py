from billing_module.crud import *
def Billing_module():
    while True:
        print("\n BILLING MENU")
        print("1. Generate Bill")
        print("2. View Bills")
        print("3. Search Bill")
        print("4. Update Payment")
        print("5. Delete Bill")
        print("6. Back")

        try:
            ch = int(input("Enter choice: "))

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
                    print("Returning to Menu...")
                    break
                case _:
                    print("Invalid Choice")

        except Exception as e:
            print("Enter a numerical value:", e)