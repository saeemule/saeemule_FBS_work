print('Series Programs')
print('a. 1! + 2! + 3! + ... + n!')
print('b. N + N^2 + N^3 + ... + N^N')
print('c. Geometric series (ratio = 2) sum of n terms')
print('d. S = a + a^2/2 + a^3/3 + ... + a^10/10')
print('e. x - x^2/3 + x^3/5 - x^4/7 + ... to n terms')

choice = input('\nEnter which series you want to run (a/b/c/d/e): ')

if choice == 'a':
    n = int(input('Enter value of n: '))
    total = 0
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i
        total = total + fact

    print(f'Sum of series (1! + 2! + ... + {n}!) = {total}')

elif choice == 'b':
    N = int(input('Enter value of N: '))
    total = 0

    for i in range(1, N + 1):
        total = total + N ** i

    print(f'Sum of series (N + N^2 + ... + N^N) = {total}')

elif choice == 'c':
    n = int(input('Enter number of terms (n): '))
    ratio = 2
    term = 1
    total = 0

    for i in range(n):
        total = total + term
        term = term * ratio

    print(f'Sum of geometric series (ratio 2) up to {n} terms = {total}')

elif choice == 'd':
    a = float(input('Enter value of a: '))
    total = 0

    for i in range(1, 11):
        total = total + (a ** i) / i

    print(f'S = a + a^2/2 + ... + a^10/10 = {total:.4f}')

elif choice == 'e':
    x = float(input('Enter value of x: '))
    n = int(input('Enter number of terms (n): '))
    total = 0
    sign = 1

    for i in range(1, n + 1):
        denominator = 2 * i - 1
        total = total + sign * (x ** i) / denominator
        sign = sign * -1

    print(f'Sum of series to {n} terms = {total:.4f}')

else:
    print('Invalid choice. Please enter a, b, c, d or e.')