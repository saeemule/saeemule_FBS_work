length = float(input("Enter length of wall (in meters): "))
height = float(input("Enter height of wall (in meters): "))
cost_per_sq_meter = float(input("Enter painting cost per sq meter: "))

num_walls = 4

area_of_one_wall = length * height
total_area = area_of_one_wall * num_walls

total_cost = total_area * cost_per_sq_meter

print(f"Area of one wall = {area_of_one_wall} sq meters")
print(f"Total area (4 walls) = {total_area} sq meters")
print(f"Total Painting Cost = Rs {total_cost:.2f}")