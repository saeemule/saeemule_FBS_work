numbers = [3, 7, 2, 9, 4, 1]
num_set = set(numbers)

sorted_nums = sorted(num_set, reverse=True)
max_product = sorted_nums[0] * sorted_nums[1]

print("List =", numbers)
print("Two numbers with maximum product =", sorted_nums[0], "and", sorted_nums[1])
print("Maximum product =", max_product)