numbers = [10, 15, 22, 33, 40, 51, 68]
even_list = []
odd_list = []
for num in numbers:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)
print("Even elements list =", even_list)
print("Odd elements list =", odd_list)