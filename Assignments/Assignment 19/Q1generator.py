def fibonacci_generator(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


# ---- Demo ----
limit = int(input("Enter the limit: "))
for num in fibonacci_generator(limit):
    print(num, end=' ')
print()