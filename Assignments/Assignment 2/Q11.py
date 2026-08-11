amount = int(input('Enter the amount = '))

notes_2000 = amount // 2000
amount = amount % 2000

notes_500 = amount // 500
amount = amount % 500

notes_200 = amount // 200
amount = amount % 200

notes_100 = amount // 100
amount = amount % 100

notes_50 = amount // 50
amount = amount % 50

notes_10 = amount // 10
amount = amount % 10

print(f'Notes of 2000 is {notes_2000}.')
print(f'Notes of 500 is {notes_500}.')
print(f'Notes of 200 is {notes_200}.')
print(f'Notes of 100 is {notes_100}.')
print(f'Notes of 50 is {notes_50}.')
print(f'Notes of 10 is {notes_10}.')