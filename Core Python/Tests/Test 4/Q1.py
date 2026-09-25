def print_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    print(f"Factors of {num} : {','.join(map(str, factors))}")


# ---- Demo ----
n = int(input("Enter a number: "))
print_factors(n)