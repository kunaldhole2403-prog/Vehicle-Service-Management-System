from connectiondb import *
def create_user():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    query = """INSERT INTO Login(username,password)
    VALUES(%s,%s)"""
