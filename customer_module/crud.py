from db import conn,cursor 

# add customer
def add_customer():
    customer_id=int(input(" enter customer ID:"))
    customer_name=input(" enter your name:")
    phone=input(" enter your phone number:")
    email=input(" enter your email:")
    address=input(" enter your address:")
   

    query=" insert into customer(customer_id,customer_name,phone,email,address) values(%s,%s,%s,%s,%s)"
    values=(customer_id,customer_name,phone,email,address)
    cursor.execute(query,values)
    conn.commit()
    print(" data added !")


# search customer

def search_customer():
    customer_id=int(input(" enter customer ID:"))
    query=" select * from customer where customer_id=%s"
    cursor.execute(query,(customer_id,))
    row=cursor.fetchone()
    if row:
        print(row)
    else:
        print(" customer not found")    


# update customer

def update_customer():
    customer_id=int(input(" enter customer ID:"))
    customer_name=input(" enter new name:")
    phone=input(" enter new phone number :")
    email=input(" enter your email:")
    address=input(" enter your address:")
   
    query="update customer set customer_name=%s,phone=%s,email=%s,address=%s where customer_id=%s"
    values=(customer_name,phone,email,address, customer_id)
    cursor.execute(query,values)
    conn.commit()
  
    if cursor.rowcount>0:
        print(" customer data updated successfully !")
    else:
        print(" customer id notfound!") 


# delete customer

def delete_customer():
    customer_id=int(input(" enter your customer ID:"))
    query=" delete from customer where customer_id=%s"
    cursor.execute(query,(customer_id,))
    conn.commit()
    if cursor.rowcount>0:
        print(" customer data deleted successfully !")
    else:
        print("customer id not found!")    


# display all data
def display_all_customer():
    query="select * from customer"
    cursor.execute(query)
    rows=cursor.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print(" no customer records found !")                

        


