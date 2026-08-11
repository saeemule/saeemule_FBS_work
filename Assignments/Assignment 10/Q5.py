numbers = [10, 20, 30, 20, 40, 20]
element = int(input("Enter a number to search: "))
count = 0
for i in range(len(numbers)):
    if numbers[i] == element:
        count += 1
if count > 0:
    print(element, "is present", count, "times in the list")
else:
    print(element, "is not present in the list")