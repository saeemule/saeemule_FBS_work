for i in range(1, 6):
    print(' ' * (5 - i), end='')
    if i == 1:
        print('*')
    else:
        print('*' + ' ' * (2 * (i - 1) - 1) + '*')

for i in range(5, 0, -1):
    print(' ' * (5 - i), end='')
    if i == 1:
        print('*')
    else:
        print('*' + ' ' * (2 * (i - 1) - 1) + '*')