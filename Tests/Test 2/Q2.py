num = input("Enter a 3-digit number: ")

if len(num) == 3 and num.isdigit():
    d1 = int(num[0])
    d2 = int(num[1])
    d3 = int(num[2])

    if d1 == 2 * d2 and d3 == 2 * d1:
        print("Yes, you have done it")
    else:
        print("Please try next time")
else:
    print("Please enter a valid 3-digit number")