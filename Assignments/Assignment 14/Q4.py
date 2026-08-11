numbers = [2, 4, 3, 5, 7, 8, 1]
target = int(input("Enter target sum: "))

seen = set()
pairs = set()
for num in numbers:
    complement = target - num
    if complement in seen:
        pair = tuple(sorted((num, complement)))
        pairs.add(pair)
    seen.add(num)

print("Pairs with sum", target, "=", pairs)