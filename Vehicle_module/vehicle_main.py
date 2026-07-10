from Vehicle_module.crud import *
def vehical_module():
    while True:

        print("\n1. Add Vehicle")
        print("2. View Vehicle")
        print("3. Search Vehicle")
        print("4. Update Vehicle")
        print("5. Delete Vehicle")
        print("6. Back")

        choice = input("Enter Choice : ")

        if choice == "1":
            add()

        elif choice == "2":
            view()

        elif choice == "3":
            search()

        elif choice == "4":
            update()

        elif choice == "5":
            delete()

        elif choice == "6":
            print("Returning to Menu....")
            break

        else:
            print("Invalid Choice")