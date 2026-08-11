def fibonacci_series(n):
    series = []
    a, b = 1, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

n = int(input("Enter number of terms: "))
print("Fibonacci Series:", fibonacci_series(n))