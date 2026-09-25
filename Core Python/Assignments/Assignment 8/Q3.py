def sum_natural_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("Enter n: "))
print("Sum =", sum_natural_numbers(n))

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

def sum_of_factorials(n):
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)
    return total

n = int(input("Enter n: "))
print("Sum =", sum_of_factorials(n))

def sum_of_powers(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total

n = int(input("Enter n: "))
print("Sum =", sum_of_powers(n))
