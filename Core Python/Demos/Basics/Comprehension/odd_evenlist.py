l1 = [3,9,18,45,20]
l2 = []
for i in l1:
    if i%2==0:
        l2.append("Even")
    else:
        l2.append("Odd")
print(l2)

print("---BY using comprehension")
l3 = ["Even" if i%2==0 else "Odd" for i in l1]
print(l3)