text = input("Enter a string: ")
words = text.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word frequency dictionary =", frequency)
for word, count in frequency.items():
    print(f"'{word}' appears {count} time(s)")