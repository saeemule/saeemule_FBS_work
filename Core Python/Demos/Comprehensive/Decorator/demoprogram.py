#
# def demo():
    # print('I am in demo')
# a=12
# b=demo
# print("type of demo=",type(demo))
# print("type of b=",type(b))
# demo()
# b()






#pass the function as an argument to another function
# def fun1():
#     print('I am from function 1')
# #fun1
# def demofun(a):
#     print('I am from demofun')
#     a()
# demofun(fun1)





#Return inner function from outer function

# def outer():
#     print("Outer is called")
#     def innerFunction():
#         print("Inner function is called")
#     return innerFunction
# a=outer()
# a()


#Closure

# def outer():
#     print("Outer is called")
#     var="virat"
#     def innerFunction():
#         print("Inner function is called",var)
#     return innerFunction
# a=outer()
# a()


#Decorator
def demo(fun):
    print("Decorator is called")
    def wrapper():
        print("Before calling your function all task will be performed here")
        fun()
        print("After calling your function all task will be performed here")
    return wrapper()
@demo
def login():
    print("\n Login is done")

@demo
def logout():
    print("\n Logout is done")
        