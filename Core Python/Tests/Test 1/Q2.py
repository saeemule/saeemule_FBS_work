principal = float(input("Enter Principal amount: "))
rate = float(input("Enter Rate of interest: "))
time = float(input("Enter Time (in years): "))

simple_interest = (principal * rate * time) / 100

print(f"Simple Interest = {simple_interest:.2f}")