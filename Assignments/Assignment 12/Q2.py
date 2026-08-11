text = input("Enter a string: ")
n = int(input("Enter index to remove: "))
result = text[:n] + text[n + 1:]
print("Result =", result)