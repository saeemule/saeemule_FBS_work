n = 5

# width of the last (merged) row = reference for alignment
last_row = ' '.join(str(x) for x in range(1, n + 1)) + ' ' + ' '.join(str(x) for x in range(n - 1, 0, -1))
full_width = len(last_row)

for i in range(1, n + 1):
    left = ' '.join(str(x) for x in range(1, i + 1))
    
    if i < n:
        right = ' '.join(str(x) for x in range(i, 0, -1))
        gap_len = full_width - len(left) - len(right)
        print(left + ' ' * gap_len + right)
    else:
        print(last_row)