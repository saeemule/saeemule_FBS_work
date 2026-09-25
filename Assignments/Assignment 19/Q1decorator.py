import functools
import time


def memoize(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"Fetching from cache for {args}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper


@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# ---- Demo ----
start = time.time()
print("Fibonacci(30):", fibonacci(30))
print("Time taken:", time.time() - start, "seconds")

# Calling again to show cache is used
start = time.time()
print("Fibonacci(30) again:", fibonacci(30))
print("Time taken:", time.time() - start, "seconds")