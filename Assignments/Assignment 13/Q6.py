numbers = {"a": 2, "b": 3, "c": 4, "d": 5}
product = 1
for key in numbers:
    product *= numbers[key]
print("Dictionary =", numbers)
print("Product of all items =", product)