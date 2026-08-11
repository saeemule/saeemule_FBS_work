def sum_of_digits(num):
    if num == 0:
        return 0
    return num % 10 + sum_of_digits(num // 10)

num = int(input("Enter a number: "))
print("Sum of digits =", sum_of_digits(abs(num)))