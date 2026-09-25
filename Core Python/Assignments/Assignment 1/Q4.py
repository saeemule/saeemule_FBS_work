#Take input from P,R,T
P = int(input('Enter Principal:'))
R = int(input('Enter Rate of Interest:'))
T = int(input('Enter Time :'))

#Perform Simple Interest
SimpleInterest = (P*R*T)/100

#Perform result
print(f'Simple Interest of {P} & {R} & {T} is {SimpleInterest}.')