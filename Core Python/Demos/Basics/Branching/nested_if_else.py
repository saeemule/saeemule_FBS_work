gender = input('Enter gender (m/f) : ')
age = int(input('Enter age : '))

if(gender == 'f'):
    if(age>=18):
        print(f'Girl is eligible for marriage.')
    else:
        print(f'Pehle padhai kar lo.')