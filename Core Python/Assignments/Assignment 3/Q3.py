a = int(input("Enter angle 1: "))
b = int(input("Enter angle 2: "))
c = int(input("Enter angle 3: "))

if a + b + c == 180 and a > 0 and b > 0 and c > 0:
    print("Triangle is Valid")
else:
    print("Triangle is Not Valid")