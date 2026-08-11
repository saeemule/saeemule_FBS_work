n = int(input("Enter number of elements: "))
numbers = []
for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    numbers.append(value)

even_list = []
odd_list = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_list.append(numbers[i])
    else:
        odd_list.append(numbers[i])

print("Even elements list =", even_list)
print("Odd elements list =", odd_list)