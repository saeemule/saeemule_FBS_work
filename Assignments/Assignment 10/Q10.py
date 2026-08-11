numbers = [10, 20, 30, 20, 40, 20, 50]
element = int(input("Enter element to remove: "))
result_list = []
for i in range(len(numbers)):
    if numbers[i] != element:
        result_list.append(numbers[i])
print("List after removing all occurrences =", result_list)