# Accept area of one wall (assumed same for all walls)
wall_area = float(input("Enter area of one wall (sq units): "))

# Accept cost per sq unit for interior and exterior painting
interior_cost_per_unit = float(input("Enter cost of interior painting per sq unit: "))
exterior_cost_per_unit = float(input("Enter cost of exterior painting per sq unit: "))

# For two joint rooms (upper view), total walls = 8 outer walls forming the L-shape
# Interior walls = 1 (the shared/common wall between the two rooms)
# Exterior walls = 7 (remaining outer boundary walls)
interior_walls = 1
exterior_walls = 7

total_interior_area = interior_walls * wall_area
total_exterior_area = exterior_walls * wall_area

interior_cost = total_interior_area * interior_cost_per_unit
exterior_cost = total_exterior_area * exterior_cost_per_unit

total_cost = interior_cost + exterior_cost

print(f"Total Interior Wall Area = {total_interior_area} sq units")
print(f"Total Exterior Wall Area = {total_exterior_area} sq units")
print(f"Interior Painting Cost = {interior_cost:.2f}")
print(f"Exterior Painting Cost = {exterior_cost:.2f}")
print(f"Total Painting Cost = {total_cost:.2f}")