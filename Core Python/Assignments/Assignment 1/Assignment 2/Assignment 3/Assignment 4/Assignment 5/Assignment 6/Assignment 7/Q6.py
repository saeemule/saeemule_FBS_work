n = 5
for i in range(1, n + 1):
    if i == 1:
        print(" ".join(str(j) for j in range(1, n + 1)))
    elif i == n:
        print(n)
    else:
        gap = " " * (2 * (n - i) - 1)
        print(f"{i}{gap}{n}")