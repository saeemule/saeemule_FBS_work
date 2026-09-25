for i in range(1, 6):
    print(' ' * (2 * (5 - i)), end='')
    for j in range(2 * i - 1):
        print(chr(65 + j), end=' ')
    print()