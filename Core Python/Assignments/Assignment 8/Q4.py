def sum_of_odd_numbers(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            total += i
    return total

n = int(input("Enter n: "))
print("Sum of odd numbers =", sum_of_odd_numbers(n))