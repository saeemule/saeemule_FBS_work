for i in range(1, 6):
    print(' ' * (2 * (5 - i)), end='')
    for k in range(i, 2 * i):
        print(k, end=' ')
    for k in range(2 * i - 2, i - 1, -1):
        print(k, end=' ')
    print()