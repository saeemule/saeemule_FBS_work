#1. structure : denoted by []
li = [10, 30, 40, 20]
print(type(li))

#2. type of data : heterogeneous
li = [10, 3.14, 'abc']
print(li)

#3. sequence : ordered

#4. changable : mutable
print(id(li))
li[1] = 17.63
print(id(li))
print(li)

#5. duplication allowed
li = [10, 10, 20, 30, 20, 10]
print(li)