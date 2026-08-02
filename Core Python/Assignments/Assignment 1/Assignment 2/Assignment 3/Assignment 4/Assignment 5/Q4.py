start = int(input('Enter start of range: '))
end = int(input('Enter end of range: '))

print(f'Armstrong numbers between {start} and {end}:')

for num in range(start, end + 1):
    temp = num
    num_of_digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + digit ** num_of_digits
        temp = temp // 10

    if total == num:
        print(num)