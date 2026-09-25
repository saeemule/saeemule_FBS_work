def chkPalindrome(num):
    temp = num
    rev = 0
    while(temp > 0):
        d = temp % 10
        rev = rev * 10 + d
        temp //= 10
    if(num == rev):
        return True
    else:
        return False

data = [123, 545, 8668, 22324, 83838]

res = list(map(chkPalindrome, data))

print(res)