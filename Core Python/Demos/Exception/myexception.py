class MyException(Exception):
    def __init__(self,*args):
        print("I am from exception")
    def __str__(self):
        return "My exception object"
