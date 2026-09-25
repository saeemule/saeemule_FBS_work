numbers = [10, 15, 20, 30, 45, 60, 90]
m = int(input("Enter value of m: "))
n = int(input("Enter value of n: "))
result_list = []
for i in range(len(numbers)):
    if numbers[i] % m == 0 and numbers[i] % n == 0:
        result_list.append(numbers[i])
print("Numbers divisible by both", m, "and", n, "=", result_list)