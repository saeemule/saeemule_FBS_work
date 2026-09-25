rows = 10
width = 22

# Top row - full line of stars
print("*" * width)

# Diagonal - single star moving left with each row (indent decreasing)
for i in range(rows):
    spaces = width - i - 2
    print(" " * spaces + "*")

# Bottom row - full line of stars plus one extra star
print("*" * width + " *")