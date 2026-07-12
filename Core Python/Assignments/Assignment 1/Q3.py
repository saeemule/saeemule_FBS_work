#Take input from dividend and divisor
dividend = int(input('Enter dividend:'))
divisor = int(input('Enter divisor:'))

#Perform calculation
quotient = dividend // divisor
remainder = dividend % divisor

#Display result
print(f'Quotient of {dividend} & {divisor} is {quotient}.') 
print(f'Remainder of {dividend} & {divisor} is {remainder}.')