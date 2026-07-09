from crud import *


# calling

print(" 1. Add customer \n 2. Search Customer \n 3.Update Customer \n 4.Delete Customer \n 5.display_all_customer \n 6. Exit")
choice=int(input(" enter your choice :"))
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
   print(" Exit")        
else:
   print(" Invalid choice")
