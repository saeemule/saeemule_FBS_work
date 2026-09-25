l1 = [x for x in range(1,9)]
#print(l1)

l2 = [x*10 for x in range(1,9)]
#print(l2)

l3 = [x*x for x in l2]
#print(l3)

l4 = [x**3 for x in l1]
#print(l4)

print("---By using traditional way")
start = int(input("enter start: "))
end = int(input("Enter end: "))
list = []
for i in range(start,end+1):
    list.append(i**0.5)
print(list)

print("---By using Comprehension")
l5 = [x**0.5 for x in range(start,end+1)]
print(l5)