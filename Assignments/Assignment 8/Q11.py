def is_armstrong(num):
    num = abs(num)
    digits = str(num)
    power = len(digits)
    total = 0
    for d in digits:
        total += int(d) ** power
    return total == num

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")