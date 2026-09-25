def add():
    try:
        a=int(input("Enter number"))
        return a
    except Execution as e:
        print(e)
        return
    finally:
        print("All are done")
        
result=add()
print(result)

    


 