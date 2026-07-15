total_amount = 0

for i in range(1, 6):
    age = int(input(f"Enter age of person {i}: "))
    ticket = float(input(f"Enter ticket amount for person {i}: "))

    if age < 12:
        amount = ticket - (ticket * 0.30)
    elif age > 59:
        amount = ticket - (ticket * 0.50)
    else:
        amount = ticket

    total_amount += amount

print(f"Total ticket amount for all 5 people = {total_amount}")