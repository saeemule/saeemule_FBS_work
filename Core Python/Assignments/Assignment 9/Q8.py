def check_prime(num, divisor=2):
    if num < 2:
        return False
    if divisor * divisor > num:
        return True
    if num % divisor == 0:
        return False
    return check_prime(num, divisor + 1)

num = int(input("Enter a number: "))
if check_prime(num):
    print(num, "is a Prime number")
else:
    print(num, "is NOT a Prime number")