def reverse_number(num):
    reverse = 0
    num = abs(num)
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10
    return reverse

num = int(input("Enter a number: "))
print("Reversed number =", reverse_number(num))