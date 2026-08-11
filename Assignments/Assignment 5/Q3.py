num_passengers = int(input('Enter number of passengers: '))
ticket_cost = float(input('Enter cost per ticket: '))

total_amount = 0

for i in range(1, num_passengers + 1):
    age = int(input(f'Enter age of passenger {i}: '))

    if age < 12:
        discount = 30
    elif age > 59:
        discount = 50
    else:
        discount = 0

    amount = ticket_cost - (ticket_cost * discount / 100)
    total_amount = total_amount + amount

    print(f'Passenger {i} (age {age}) -> Discount: {discount}% -> Amount to pay: {amount:.2f}')

print(f'\nTotal amount for all passengers: {total_amount:.2f}')