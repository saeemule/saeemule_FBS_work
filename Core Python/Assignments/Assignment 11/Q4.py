numbers = [12, 45, 2, 89, 33, 7]
n = len(numbers)

# Bubble Sort (ascending order)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list =", numbers)
print("Second largest number =", numbers[n - 2])