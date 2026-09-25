print("---By using traditional way")
start = int(input("enter start: "))
end = int(input("Enter end: "))
list = []
for i in range(start,end+1):
    if i%2!=0:
        list.append(i**2)
print(list)

print("---By using Comprehension")
l5 = [x**2 for x in range(start,end+1) if x%2!=0]
print(l5)