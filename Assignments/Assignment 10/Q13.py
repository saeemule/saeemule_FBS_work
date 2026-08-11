numbers = [10, 15, 22, 33, 40, 51, 68]
result_list = []
for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        result_list.append(numbers[i])
print("List after removing even numbers =", result_list)