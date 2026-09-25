num = 379

#temp = num

d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10

sum = d1 + d2 + d3
print(f'Sum of three digit number is {sum}')
