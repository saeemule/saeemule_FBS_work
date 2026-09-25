def palindrome_generator():
    num = 0
    while True:
        if str(num) == str(num)[::-1]:
            yield num
        num += 1


# ---- Demo ----
count = int(input("How many palindromes do you want? "))
gen = palindrome_generator()
for _ in range(count):
    print(next(gen), end=' ')
print()