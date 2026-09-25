text = input("Enter a string: ")
result = ""
for i in range(len(text)):
    if i % 2 == 0:
        result += text[i]
print("Result =", result)