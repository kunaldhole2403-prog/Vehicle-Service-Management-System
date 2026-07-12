from Login.login import *
from customer_module.main import customer_menue
from Login.forget_pass import *
from Login.connectiondb import *
from Vehicle_module.crud import *
from Vehicle_module.vehicle_main import *
from billing_module.crud import *
from billing_module.menu import *
from billing_module.db import conn, cursor
from Vehicle_module.db import conn, cursor
from Service_module.db import *
from Service_module.curd import *
from Service_module.service_main import *

while True:

    print("\n===== LOGIN SYSTEM =====")
    print("1. Create New User")
    print("2. Login")
    print("3. Forget Password")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        create_user()

    elif choice == "2":

        user = login()

        if user:

            while True:

                print("\n===== ACCOUNT MENU =====")
                print("1. Change Password")
                print("2. Delete Account")
                print("3. Vehicle Service Management System")
                print("4. Logout")

                ch = input("Enter Choice: ")

                if ch == "1":
                    change_password(user)

                elif ch == "2":

                    if delete_account(user):
                        break

                elif ch == "3":

                    while True:

                        print("\n===== VEHICLE SERVICE MANAGEMENT =====")
                        print("1. Customer Module")
                        print("2. Vehicle Module")
                        print("3. Service Module")
                        print("4. Billing Module")
                        print("5. Back")

                        op = input("Enter Choice: ")

                        if op == "1":
                            customer_menue()

                        elif op == "2":
                            vehicle_menu()

                        elif op == "3":
                            service_menu()

                        elif op == "4":
                            billing_menu()

                        elif op == "5":
                            break

                        else:
                            print("Invalid Choice")

                elif ch == "4":
                    print("Logged Out Successfully")
                    break

                else:
                    print("Invalid Choice")

    elif choice == "3":
        forget_pass()

    elif choice == "4":
        print("Thank You")
        break

    else:
        print("Invalid Choice")