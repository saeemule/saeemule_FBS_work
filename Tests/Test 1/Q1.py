import math

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
radius = float(input("Enter radius: "))

# Area = Rectangle area + Semicircle area
area = (length * breadth) + (0.5 * math.pi * radius ** 2)

# Perimeter = 2 straight sides (top+bottom) + 1 straight side (left) + curved arc (semicircle)
perimeter = (2 * length) + breadth + (math.pi * radius)

print(f"Area = {area:.2f} sq units")
print(f"Perimeter = {perimeter:.2f} units")