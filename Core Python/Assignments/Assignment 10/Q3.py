numbers = [12, 45, 2, 89, 33, 7]
largest = second_largest = float('-inf')
for i in range(len(numbers)):
    if numbers[i] > largest:
        second_largest = largest
        largest = numbers[i]
    elif numbers[i] > second_largest and numbers[i] != largest:
        second_largest = numbers[i]
print("Second largest element =", second_largest)