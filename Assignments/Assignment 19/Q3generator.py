def my_range(start, stop, step=1):
    if step == 0:
        raise ValueError("step must not be zero")
    current = start
    if step > 0:
        while current < stop:
            yield current
            current += step
    else:
        while current > stop:
            yield current
            current += step


# ---- Demo ----
print("my_range(1, 10):")
for i in my_range(1, 10):
    print(i, end=' ')
print()

print("my_range(0, 20, 3):")
for i in my_range(0, 20, 3):
    print(i, end=' ')
print()

print("my_range(10, 0, -2):")
for i in my_range(10, 0, -2):
    print(i, end=' ')
print()