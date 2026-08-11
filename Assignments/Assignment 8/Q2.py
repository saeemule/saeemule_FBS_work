import math

def area_of_circle(radius):
    return math.pi * radius * radius

radius = float(input("Enter radius: "))
print("Area of Circle =", round(area_of_circle(radius), 2))