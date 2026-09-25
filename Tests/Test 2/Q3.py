import math

radius = 20      # meters (circular section)
length = 50       # meters (rectangle length)
breadth = 40      # meters (rectangle breadth)
cost_per_meter = 35   # Rs per meter
times = 5         # fencing done 5 times

# Perimeter of the field = 2 lengths + 1 breadth + semicircle arc (curved end)
perimeter = (2 * length) + breadth + (math.pi * radius)

# Total wire needed since fencing is done 5 times
total_wire_length = perimeter * times

# Total cost
total_cost = total_wire_length * cost_per_meter

print(f"Perimeter of field = {perimeter:.2f} m")
print(f"Total wire length needed (5 times) = {total_wire_length:.2f} m")
print(f"Total cost of fencing = Rs {total_cost:.2f}")