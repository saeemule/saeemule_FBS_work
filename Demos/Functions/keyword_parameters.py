def emp(id, name, sal, dept):
    data = 'ID:' + str(id) + '\n'
    data += 'NAME:'+ str(name) + '\n'
    data += 'SALARY:'+str(sal) + '\n'
    data += 'DEPARTMENT:'+ str(dept) + '\n'
    return data

res = emp(name = 'SAEE', id = 101 , dept = 'IT', sal = 20000)
print(res)
    
    

