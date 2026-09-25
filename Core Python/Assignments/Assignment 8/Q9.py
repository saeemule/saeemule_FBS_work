def reverse_number(num):
    reverse = 0
    num = abs(num)
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10
    return reverse

def is_palindrome(num):
    return num == reverse_number(num)

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(num, "is a Palindrome number")
else:
    print(num, "is NOT a Palindrome number")