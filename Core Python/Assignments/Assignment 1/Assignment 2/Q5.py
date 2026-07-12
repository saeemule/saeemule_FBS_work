costprice = float(input("Enter cost price = "))
discount = float(input("Enter discount percentage = "))

selling_price = costprice - (costprice * discount / 100)

print(f'Selling price is {selling_price}')