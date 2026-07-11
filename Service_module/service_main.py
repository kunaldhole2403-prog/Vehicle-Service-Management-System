from Service_module.curd import *
def service_menu():

    while True:

        print("\n===== SERVICE MODULE =====")

        print("1. Add Service")
        print("2. View Services")
        print("3. Search Service")
        print("4. Update Service Status")
        print("5. Delete Service")
        print("6. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_service()

        elif choice == "2":
            view_services()

        elif choice == "3":
            search_service()

        elif choice == "4":
            update_service()

        elif choice == "5":
            delete_service()

        elif choice == "6":
            break

        else:
            print("Invalid Choice")