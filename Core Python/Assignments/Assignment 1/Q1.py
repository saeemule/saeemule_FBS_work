#Take input of marks
sub1 = float(input('Enter marks of subject 1: '))
sub2 = float(input('Enter marks of subject 2: '))
sub3 = float(input('Enter marks of subject 3: '))
sub4 = float(input('Enter marks of subject 4: '))
sub5 = float(input('Enter marks of subject 5: '))

#Perform calculation
total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5

#Display result
print(f'Total marks is {total}.')
print(f'Percentage of student is {percentage}%.')