numbers = [10, 20, 10, 30, 20, 40, 10]
unique_list = []
for i in range(len(numbers)):
    found = False
    for j in range(len(unique_list)):
        if numbers[i] == unique_list[j]:
            found = True
            break
    if not found:
        unique_list.append(numbers[i])
print("List after removing duplicates =", unique_list)