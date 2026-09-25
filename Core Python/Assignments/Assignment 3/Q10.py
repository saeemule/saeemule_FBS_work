gender = input("Enter gender (male/female): ")
age = int(input("Enter age: "))

if gender == "male" and age >= 21:
    print("Eligible to Marry")
elif gender == "female" and age >= 18:
    print("Eligible to Marry")
else:
    print("Not Eligible to Marry")