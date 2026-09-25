divisible_by_any_digit = [num for num in range(1, 1001) if any(num % d == 0 for d in range(1, 10))]
print(divisible_by_any_digit)