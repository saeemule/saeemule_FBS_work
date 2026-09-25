n = int(input("Enter number of employees: "))

total_salary_all_emp = 0

for i in range(1, n + 1):
    basic = float(input(f"\nEnter basic salary of employee {i}: "))

    if basic < 20000:
        da = basic * 10 / 100
        ta = basic * 12 / 100
        hra = basic * 15 / 100
    else:
        da = basic * 15 / 100
        ta = basic * 18 / 100
        hra = basic * 20 / 100

    total_salary = basic + da + ta + hra
    total_salary_all_emp += total_salary

    print(f"Employee {i} -> Basic: {basic}, DA: {da}, TA: {ta}, HRA: {hra}, Total Salary: {total_salary:.2f}")

print(f"\nTotal Salary of all employees = {total_salary_all_emp:.2f}")