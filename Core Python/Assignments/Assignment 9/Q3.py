def reverse_number(num, reverse=0):
    if num == 0:
        return reverse
    digit = num % 10
    reverse = reverse * 10 + digit
    return reverse_number(num // 10, reverse)

num = int(input("Enter a number: "))
print("Reversed number =", reverse_number(num))