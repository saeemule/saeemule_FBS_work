import math

n = int(input("Enter the value of N: "))

total_sum = 0
for i in range(1, n + 1):
    factorial = math.factorial(i)
    term = i / factorial
    total_sum += term

print(f"Sum of the series = {total_sum:.4f}")