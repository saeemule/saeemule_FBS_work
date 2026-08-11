text = input("Enter a string: ")
result = ""
for ch in text:
    if ch == 'a':
        result += '$'
    else:
        result += ch
print("Result =", result)