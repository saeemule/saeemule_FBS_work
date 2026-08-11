correct_id = 'admin'
correct_password = 'admin123'

attempts = 3

for i in range(attempts):
    userid = input('Enter userid: ')
    password = input('Enter password: ')

    if userid == correct_id and password == correct_password:
        print('Login successful!')
        break
    else:
        remaining = attempts - i - 1
        if remaining > 0:
            print(f'Incorrect userid or password. You have {remaining} attempt(s) left.')
        else:
            print('You have used all 3 attempts. Program terminated.')