#Take input from P,R,T
P = int(input('Enter Principal:'))
R = int(input('Enter Rate of Interest:'))
T = int(input('Enter Time :'))

#Perform Simple Interest
SimpleInterest = (P*R*T)/100

#Perform result
# print(SimpleInterest)
# print('Simple Interest :',SimpleInterest)
# print('Simple Interest is' + str(SimpleInterest))
print(f'Simple Interest of {P} & {R} & {T} is {SimpleInterest}.')
