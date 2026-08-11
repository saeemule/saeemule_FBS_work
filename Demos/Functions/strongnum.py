def chkStrong():
    num = int(input('Enter number :'))
    temp = num
    sum = 0

    while( temp > 0):
        d = temp % 10
        fact = 1

        i = 1
        while(i <= d):
            fact = fact * i
            i = i + 1

            sum = sum + fact
            temp = temp // 10

        if ( num == sum ):
            print('The number is strong number.')
        else:
            print('The number is not strong number.')

chkStrong()