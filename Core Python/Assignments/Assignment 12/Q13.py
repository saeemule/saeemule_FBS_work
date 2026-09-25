text = input("Enter a string: ")
digit_count = 0
letter_count = 0
for ch in text:
    if ch.isdigit():
        digit_count += 1
    elif ch.isalpha():
        letter_count += 1
print("Number of digits =", digit_count)
print("Number of letters =", letter_count)