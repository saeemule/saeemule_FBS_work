start = int(input('Enter start of range: '))
end = int(input('Enter end of range: '))
div = int(input('Enter the divisor: '))

for i in range(start, end+1):
    if(i % div == 0):
        print(i)