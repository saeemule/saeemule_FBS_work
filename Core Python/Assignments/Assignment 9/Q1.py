def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

def sum_of_factorials(n):
    if n == 1:
        return factorial(1)
    return factorial(n) + sum_of_factorials(n - 1)

n = int(input("Enter n: "))
print("Sum of series =", sum_of_factorials(n))