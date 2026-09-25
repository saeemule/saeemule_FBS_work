for i in range(4):
    print(' ' * (3 - i), end='')
    value = 1
    for j in range(i + 1):
        print(value, end=' ')
        value = value * (i - j) // (j + 1)
    print()