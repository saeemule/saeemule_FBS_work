original_list = [1, 2, 3, 4, 5]
duplicate_list = []
for i in range(len(original_list)):
    duplicate_list.append(original_list[i])

# Proving they are independent
duplicate_list[0] = 100
print("Original list =", original_list)
print("Duplicate list =", duplicate_list)