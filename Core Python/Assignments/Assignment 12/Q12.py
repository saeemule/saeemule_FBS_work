text = input("Enter a string: ")
count = 0
for ch in text:
    if ch >= 'a' and ch <= 'z':
        count += 1
print("Number of lowercase characters =", count)