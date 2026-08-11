text = input("Enter a string: ")

# Count characters (excluding spaces)
char_count = 0
for ch in text:
    if ch != ' ':
        char_count += 1

# Count words
word_count = 1
for ch in text:
    if ch == ' ':
        word_count += 1

print("Number of words =", word_count)
print("Number of characters =", char_count)