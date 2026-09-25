m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
m4 = int(input("Enter marks of subject 4: "))
m5 = int(input("Enter marks of subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

if percentage >= 60:
    print(f"Percentage = {percentage}, Grade: First Class")
elif percentage >= 50:
    print(f"Percentage = {percentage}, Grade: Second Class")
elif percentage >= 40:
    print(f"Percentage = {percentage}, Grade: Third Class")
else:
    print(f"Percentage = {percentage}, Grade: Fail")