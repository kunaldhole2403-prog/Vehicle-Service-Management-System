from customer_module.crud import *

# calling
def customer_menue():
   while True:
      try:
         print(" 1. Add customer \n 2. Search Customer \n 3. Update Customer \n 4. Delete Customer \n 5. Display All customer \n 6. Back ")
         choice=int(input(" Enter your choice :"))
         if choice==1:
            add_customer()

         elif choice==2:
            search_customer()

         elif choice==3:
            update_customer()

         elif choice==4:
            delete_customer()

         elif choice==5:
            display_all_customer()

         elif choice==6:
            print("Returing to menue press")       

         else:
            print("Invalid choice")


      except ValueError:
         print(" Error: Please enter only numbers. ")

      except Exception as e:
         print(" An error occurred:",e)



