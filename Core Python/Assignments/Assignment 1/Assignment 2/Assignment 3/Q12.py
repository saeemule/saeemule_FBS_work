num = int(input("Enter a 3 digit number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print(f"{original} is a Palindrome")
else:
    print(f"{original} is Not a Palindrome")