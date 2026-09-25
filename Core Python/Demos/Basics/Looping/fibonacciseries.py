n = int(input('How many fibonacci series do you want:'))
a = -1
b = 1

for i in range(n):
    c = a+b
    print(c)
    a = b
    b = c