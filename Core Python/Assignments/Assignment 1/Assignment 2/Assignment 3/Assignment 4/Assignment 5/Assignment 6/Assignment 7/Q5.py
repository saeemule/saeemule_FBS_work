n = 5

for i in range(1, n + 1):
    # spacing before the row (centers it)
    spaces = ' ' * (n - i)
    
    row = ''
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            row += str(j) + ' '
        else:
            row += '  '
    
    print(spaces + row)