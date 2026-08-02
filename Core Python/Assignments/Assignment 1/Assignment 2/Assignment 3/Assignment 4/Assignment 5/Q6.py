n = int(input('Enter value of n: '))

count = 0
num = 2

print(f'First {n} prime numbers:')

while count < n:
    is_prime = True

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)
        count = count + 1

    num = num + 1