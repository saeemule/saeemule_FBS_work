numbers = [12, 45, 2, 89, 33, 7]
maximum = numbers[0]
minimum = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > maximum:
        maximum = numbers[i]
    if numbers[i] < minimum:
        minimum = numbers[i]
print("Maximum =", maximum)
print("Minimum =", minimum)