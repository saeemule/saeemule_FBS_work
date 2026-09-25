n = int(input("Enter n: "))
square_dict = {}
for x in range(1, n + 1):
    square_dict[x] = x * x
print("Dictionary =", square_dict)