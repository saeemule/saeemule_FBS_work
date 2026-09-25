numbers = [1, 2, 3, 4, 5, 6, 7]
target = int(input("Enter target sum: "))

n = len(numbers)
result = set()

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if numbers[i] + numbers[j] + numbers[k] == target:
                combo = tuple(sorted((numbers[i], numbers[j], numbers[k])))
                result.add(combo)

print("Unique combinations of 3 numbers summing to", target, "=", result)