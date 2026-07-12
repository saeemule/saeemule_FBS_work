basic = float(input("Enter basic salary = "))

da = basic * 10 / 100
ta = basic * 12 / 100
hra = basic * 15 / 100

total_salary = basic + da + ta + hra

print(f'Total salary is {total_salary}.')