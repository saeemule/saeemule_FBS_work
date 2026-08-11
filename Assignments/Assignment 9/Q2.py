def power_sum(temp, power, total=0):
    if temp == 0:
        return total
    digit = temp % 10
    return power_sum(temp // 10, power, total + digit ** power)

def is_armstrong(num):
    power = len(str(num))
    return power_sum(num, power) == num

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")