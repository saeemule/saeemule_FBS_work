class Distance:
    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm
        print(f"Constructor called: Distance {self.km} km {self.m} m {self.cm} cm created")

    def __del__(self):
        print(f"Destructor called: Distance {self.km} km {self.m} m {self.cm} cm destroyed")

    def __add__(self, other):
        total_cm = (self.cm + other.cm)
        total_m = (self.m + other.m)
        total_km = (self.km + other.km)

        # carry cm -> m
        total_m += total_cm // 100
        total_cm = total_cm % 100

        # carry m -> km
        total_km += total_m // 1000
        total_m = total_m % 1000

        return Distance(total_km, total_m, total_cm)

    def __sub__(self, other):
        # Convert both distances fully to cm
        total1 = (self.km * 100000) + (self.m * 100) + self.cm
        total2 = (other.km * 100000) + (other.m * 100) + other.cm

        diff = abs(total1 - total2)

        km = diff // 100000
        diff = diff % 100000
        m = diff // 100
        cm = diff % 100

        return Distance(km, m, cm)

    def __str__(self):
        return f"{self.km} km {self.m} m {self.cm} cm"


# ---- Demo ----
d1 = Distance(5, 500, 60)
d2 = Distance(3, 700, 80)

print("D1 =", d1)
print("D2 =", d2)

d3 = d1 + d2
print("D1 + D2 =", d3)

d4 = d1 - d2
print("D1 - D2 =", d4)