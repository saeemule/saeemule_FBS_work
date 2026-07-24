num = int(input('Enter the number: '))
temp = num
sum = 0
n = len(str(num))

while(temp > 0):
    d = temp % 10
    sum = sum + d**n
    temp = temp // 10

if(sum == num):
    print('Armstrong Number')
else:
    print('Not Armstrong Number')