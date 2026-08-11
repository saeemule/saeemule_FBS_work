def fibonacci(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    series = fibonacci(n - 1)
    series.append(series[-1] + series[-2])
    return series

n = int(input("Enter number of terms: "))
print("Fibonacci Series:", fibonacci(n))