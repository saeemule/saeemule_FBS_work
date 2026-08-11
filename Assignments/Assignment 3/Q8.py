import random

userId = input("Enter the user id= ")
password = input("Enter the Password = ")

if userId == "admin" and password == "virat@123":
    captch = random.randint(1000, 9999)
    print(f"Your Captcha = {captch}")
    chuser = int(input("Enter the Captcha=> "))
    if chuser == captch:
        print("User Login Successfully..")
    else:
        print("Invalid Captcha....")
else:
    print("User is Invalid")