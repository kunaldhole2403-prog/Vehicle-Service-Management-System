import smtplib
import random
import time
from Login.connectiondb import *

def send_otp(email,otp):
    sender = "t96247815@gmail.com"
    app_pass = "cxkc fahq myop jfbx"

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()

    server.login(sender ,app_pass)
    message = f"Your OTP is {otp}"
    server.sendmail(
        sender,
        email,
        message
    )
    server.quit()


def forget_pass():
    conn = get_connection()

    email = input("Enter your register Email: ")

    cursor = conn.cursor()

    query = """
    select * from login where email =%s
"""
    cursor.execute(query,(email,))
    data = cursor.fetchone()

    if not data:
        print("Email Not Found")
        cursor.close()
        conn.close()
        return
    otp = random.randint(1000,9999)

    send_otp(email, otp)
    
    print("OTP Sent Successfully ")

    print("OTP valid for 90 Second")

    start_time = time.time()

    try:
        user_otp = int(input("Enter OTP: "))
    except ValueError:
        print("Invalid OTP format")
        return 

    if time.time() - start_time > 90:
        print("OTP Expired")
        return
    if user_otp == otp:
        new_password = input("Enter New Password: ")
        confirm_password = input("Confirm Password: ")

        if new_password == confirm_password:
            query = """
            Update login set password =%s
            where email = %s
            """
            cursor.execute(query,(new_password,email))
            conn.commit()
            print("Password Updated Successfully")
        else:
            print("Password Do not Match")
    else:
        print("Invalid OTP")
    cursor.close()
    conn.close()

    