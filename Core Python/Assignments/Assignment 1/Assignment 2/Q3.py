feet = float(input("Enter feet = "))
inches = float(input("Enter inches = "))

total_inches = (feet * 12) + inches
meter = total_inches * 0.0254
centimeter = total_inches * 2.54

print(f'Meter is {meter}')
print(f'Centimeter is {centimeter}')