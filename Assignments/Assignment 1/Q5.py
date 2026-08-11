#Take input from P,R,T
P = int(input('Enter Principal:'))
R = int(input('Enter Rate of Interest:'))
T = int(input('Enter Time :'))

#Perform Simple Interest
CI = P * (1 + R / 100) ** T - P

#Perform result
print(f'Compound Interest of {P} & {R} & {T} is {CI}.')