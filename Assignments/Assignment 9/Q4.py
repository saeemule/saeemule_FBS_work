def sum_of_n_numbers(n):
    if n == 0:
        return 0
    return n + sum_of_n_numbers(n - 1)

n = int(input("Enter n: "))
print("Sum of first", n, "numbers =", sum_of_n_numbers(n))