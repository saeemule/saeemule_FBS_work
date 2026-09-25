from myexception import MyException
try:
    no1=int(input("Enter number 1:"))
    no2=int(input("Enter number 2:"))
    if no2<=0:
        raise Exception("Number proper enter nahi hua")
    else:
        print(no1/no2)
except myexception as m:
    print("myexception")
    print(m)
except Exception as e:
    print(e)