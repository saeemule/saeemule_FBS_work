try:
    no1=int(input("Enter the number1"))
    no2=int(input("Enter the number2"))
    print(no1/no2)
except ZeroDivisionError as z:
    print(z)
except ValueError as v:
    print(" Enter proper integer value")
except Exception as e:
    print("Cannot divided by zero")
else:
    print("Kuch bhi exception nhi aaya")