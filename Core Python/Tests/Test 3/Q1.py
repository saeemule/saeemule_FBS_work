def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


n = int(input("Enter how many prime numbers you want: "))

count = 0
num = 2

print(f"First {n} prime numbers are:")
while count < n:
    if is_prime(num):
        print(num, end=' ')
        count += 1
    num += 1
print()