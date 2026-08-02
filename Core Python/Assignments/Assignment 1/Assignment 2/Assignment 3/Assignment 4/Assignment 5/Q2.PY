n = int(input('Enter number of students: '))

total_percentage = 0

for i in range(1, n + 1):
    print(f'\nEnter marks for student {i} (out of 100 each):')
    total_marks = 0

    for subject in range(1, 6):
        marks = float(input(f'  Enter marks for subject {subject}: '))
        total_marks = total_marks + marks

    percentage = total_marks / 5
    total_percentage = total_percentage + percentage

    print(f'Student {i} percentage: {percentage:.2f}%')

average_percentage = total_percentage / n
print(f'\nAverage percentage of all students: {average_percentage:.2f}%')