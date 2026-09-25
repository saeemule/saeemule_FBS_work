#Take input of a, b, c
a = float(input('Enter value of a: '))
b = float(input('Enter value of b: '))
c = float(input('Enter value of c: '))

#Perform calculation using b^2 - 4ac
d = (b ** 2) - (4 * a * c)
root1 = (-b + d ** 0.5) / (2 * a)
root2 = (-b - d ** 0.5) / (2 * a)
 
# Display result
print(f'Root 1 of the equation is {root1}')
print(f'Root 2 of the equation is {root2}')