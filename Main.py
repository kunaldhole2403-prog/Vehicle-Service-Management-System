from Login.login import *
from customer_module.main import customer_menue
from Login.forget_pass import *
from Login.connectiondb import *
while True:
    print("\n===== LOGIN SYSTEM =====")
    print("1. Create New User")
    print("2. Login")
    print("3. Forget Password")
    print("4. Exit")


    choice = int(input("Enter Choice: "))

    if choice == 1:
        create_user()

    elif choice == 2:
        if login():
            print("Welcome to Vehicle Service Management System")
            print("="*60)
            print("1. Customer Menue: ")
            print("2. Vehical Menue: ")
            print("3. Service Menue: ")
            print("4. Billing Menue: ")
            try:
                choice_menue = int(input("Enter the Menue: "))
                match choice_menue:
                    case 1:
                        customer_menue()  
                    case _:
                        pass  
            except Exception as e:
                print(e)                
    elif choice == 3:
        forget_pass()

    elif choice == 4:
        break

    else:
        print("Invalid Choice")