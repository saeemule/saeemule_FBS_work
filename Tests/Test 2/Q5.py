total_price = 0

for i in range(1, 6):
    price = float(input(f"Enter price of product {i}: "))
    total_price += price

gst = (total_price * 18) / 100
total_bill = total_price + gst

print(f"Total price of products = Rs {total_price:.2f}")
print(f"GST (18%) = Rs {gst:.2f}")
print(f"Total Bill (with GST) = Rs {total_bill:.2f}")