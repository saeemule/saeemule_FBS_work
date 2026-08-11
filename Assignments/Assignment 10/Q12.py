numbers = [1, 2, 3, 4, 5]
squares = []
cubes = []
for i in range(len(numbers)):
    squares.append(numbers[i] ** 2)
    cubes.append(numbers[i] ** 3)

print("Numbers list =", numbers)
print("Squares list =", squares)
print("Cubes list =", cubes)