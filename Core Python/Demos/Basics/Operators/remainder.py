#Take input from dividend and divisor
dividend = int(input('Enter dividend:'))
divisor = int(input('Enter divisor:'))

#Perform calculation
quotient = dividend // divisor
remainder = dividend % divisor

#Display result
# print(quotient)
# print('Quotient:',quotient)
# print('Quotient is ' +  str(quotient))
print(f'Quotient of {dividend} & {divisor} is {quotient}.')

# print(remainder)
# print('Remainder:',remainder)
# print('Remainder is ' +  str(remainder))
print(f'Remainder of {dividend} & {divisor} is {remainder}.')